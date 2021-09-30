# Two Dots

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def check(x, y, color):
    global start_x, start_y, flag
    visited[x][y] = True
    visited[start_x][start_y] = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and array[nx][ny] == color:
            if nx == start_x and ny == start_y:
                flag = True
                return
            visited[nx][ny] = True
            check(nx, ny, color)
            continue
    return False

def find_start(array, color):
    for i in range(n):
        for j in range(m):
            if array[i][j] == color:
                return (i, j)


n, m = map(int, input().split())

color = set()

# 입력
array = []
for _ in range(n):
    array.append(input())

# 색깔추출
for i in range(n):
    for j in range(m):
        color.add(array[i][j])


for _ in range(len(color)):
    c = color.pop()
    start_x, start_y = find_start(array, c)
    visited = [[False] * m for _ in range(n)]
    flag = False
    check(start_x, start_y, c)
    if flag:
        break

if flag:
    print('YES')
else:
    print('NO')


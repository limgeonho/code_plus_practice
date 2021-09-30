# Two Dots

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def go(x, y, px, py, color):
    if visited[x][y]:
        return True
    visited[x][y] = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<m:
            if (nx, ny) == (px, py):
                continue
            if array[nx][ny] == color:
                if go(nx, ny, x, y, color):
                    return True
    return False

n, m = map(int, input().split())

# 입력
array = [input() for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        flag = go(i, j, -1, -1, array[i][j])
        if flag:
            print('Yes')
            exit()

print('No')


# 아기 상어

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(a, x, y, size):
    n = len(a)
    ans = []
    d = [[-1]*n for _ in range(n)] # d == visited
    q = deque()
    q.append((x, y))
    d[x][y] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n and d[nx][ny] == -1:
                ok = False
                eat = False
                # 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있음
                if a[nx][ny] == 0:
                    ok = True
                # 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있음
                elif a[nx][ny] < size:
                    ok = True
                    eat = True
                # 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있음
                elif a[nx][ny] == size:
                    ok = True
                if ok:
                    q.append((nx, ny))
                    d[nx][ny] = d[x][y] + 1
                    if eat:
                        ans.append((d[nx][ny], nx, ny))
    if not ans:
        return None
    ans.sort()
    return ans[0]


n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

x, y = 0, 0

# 상어 위치 찾기
for i in range(n):
    for j in range(n):
        if a[i][j] == 9:
            x, y = i, j
            # 0으로 바꾸는 이유 : 9는 단순하게 상어의 위치
            a[i][j] = 0


ans = 0
size = 2
exp = 0
while True:
    p = bfs(a, x, y, size)
    if p is None:
        break
    dist, nx, ny = p
    a[nx][ny] = 0
    ans += dist
    exp += 1
    if size == exp:
        size += 1
        exp = 0
    x, y = nx, ny

print(ans)
# 데스 나이트
# knight의 이동구간을 직접 설정해서 이동시키는 bfs

from collections import deque

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    chess[x][y] = 0
    while q:
        now_x, now_y = q.popleft()
        for k in range(6):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<n and 0<=ny<n and chess[nx][ny] == 0:
                chess[nx][ny] = chess[now_x][now_y] + 1
                q.append((nx, ny))


n = int(input())

array = list(map(int, input().split()))

chess = [[0]*n for _ in range(n)]

sx, se = array[0], array[1]
fx, fe = array[2], array[3]

bfs(sx, se)

if chess[fx][fe]:
    print(chess[fx][fe])
else:
    print(-1)
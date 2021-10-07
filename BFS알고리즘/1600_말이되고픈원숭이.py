# 말이 되고픈 원숭이

from collections import deque
import pprint

dx = [0, 0, 1, -1, -2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, -1, 0, 0, 1, 2, 2, 1, -1, -2, -2, -1]
cost = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]

k = int(input())
w, h = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

dist = [[[-1] *(k+1) for _ in range(w)] for _ in range(h)]

q = deque()
q.append((0, 0, 0))
dist[0][0][0] = 0

while q:
    x, y, c = q.popleft()
    for l in range(12):
        nx = x + dx[l]
        ny = y + dy[l]
        nc = c + cost[l]
        if 0<=nx<h and 0<=ny<w and a[nx][ny] == 0:
            if nc <= k:
                if dist[nx][ny][nc] == -1:
                    dist[nx][ny][nc] = dist[x][y][c] + 1
                    q.append((nx, ny, nc))

answer = -1
for i in range(k+1):
    if dist[h-1][w-1][i] == -1:
        continue
    if answer == -1 or answer > dist[h-1][w-1][i]:
        answer = dist[h-1][w-1][i]
pprint.pprint(dist)
print(answer)
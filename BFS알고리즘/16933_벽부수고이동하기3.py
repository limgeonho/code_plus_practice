# 벽 부수고 이동하기 3

import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
a = [input() for _ in range(n)]
dist = [[-1]*m for _ in range(n)]
q = deque()
answer = -1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q.append((0, 0, k, 1, 1))
while q:
    x, y, z, count, day = q.popleft()
    if (x, y) == (n-1, m-1):
        if answer == -1 or answer > count:
            answer = count
        continue
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == '1' and day:
                if dist[nx][ny] < z-1:
                    dist[nx][ny] = z-1
                    q.append((nx, ny, z-1, count+1, 0))
            elif a[nx][ny] == '0':
                if dist[nx][ny] < z:
                    dist[nx][ny] = z
                    q.append((nx, ny, z, count+1, 1-day))
    if not day:
        q.append((x, y, z, count+1, 1-day))
print(answer)
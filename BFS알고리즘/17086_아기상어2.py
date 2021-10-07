# 아기 상어2

from collections import deque

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(arr):
    q = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

bfs(a)

answer = -1

for i in a:
    tmp = max(i)
    if answer < tmp:
        answer = tmp

print(answer-1)
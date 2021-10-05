# 레이저 통신

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(sx, sy):
    q = deque()
    q.append((sx,sy))
    check[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            while 0<=nx<h and 0<=ny<w:
                if board[nx][ny] == '*':
                    break
                if check[nx][ny] == -1:
                    check[nx][ny] = check[x][y] + 1
                    q.append((nx, ny))
                nx += dx[k]
                ny += dy[k]

w, h = map(int, input().split())

board = [list(input()) for _ in range(h)]
check = [[-1] * w for _ in range(h)]

candidate = []

for i in range(h):
    for j in range(w):
        if board[i][j] == 'C':
            candidate.append((i, j))

destination = candidate[1]
dfs(candidate[0][0], candidate[0][1])

print(check[destination[0]][destination[1]]-1)
# 레이저 통신
# bfs탐색을 했을 때 한 칸 씩만 움직이는 것이 아니라 갈 수 있는 곳까지 쭉 진행(NEW!!)
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
            # ============================================
            # 갈 수 있는 곳까지 쭉 진행 => 조건내에서 계속반복해야함 => while문
            while 0<=nx<h and 0<=ny<w:
                if board[nx][ny] == '*':
                    break
                if check[nx][ny] == -1:
                    check[nx][ny] = check[x][y] + 1
                    q.append((nx, ny))
                # 범위내에서 계속 진행하는 부분(핵심)
                nx += dx[k]
                ny += dy[k]
            # ============================================
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
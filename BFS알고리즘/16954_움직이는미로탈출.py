# 움직이는 미로 탈출

from collections import deque
dx = [0, -1, -1, 0, 1, 1, -1, 0, -1]
dy = [0, 0, 1, 1, 1, 0, 1, -1, -1]

n = 8
board = [input() for _ in range(n)]
check = [[[False] * (n+1) for _ in range(n)] for _ in range(n)]

q = deque()
q.append((7, 0, 0))
ans = False

while q:
    x, y, t = q.popleft()
    if x == 0 and y == 7:
        ans = True
    for k in range(9):
        nx = x + dx[k]
        ny = y + dy[k]
        nt = min(t+1, 8)
        if 0<=nx<n and 0<=ny<n:
            if nx-t >= 0 and board[nx-t][ny] == '#':
                continue
            if nx-t-1 >= 0 and board[nx-t-1][ny] == '#':
                continue
            if check[nx][ny][nt] == False:
                check[nx][ny][nt] = True
                q.append((nx, ny, nt))

print(1 if ans else 0)

# =====================================================
from sys import stdin


def solution(board):
    WALL = '#'
    DELTA = (0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)
    N = 8

    moves = [(N - 1, 0)]  # row offset, x, y
    while True:
        visited = [[False] * N for _ in range(N)]
        new_moves = []
        for x, y in moves:
            if (x, y) == (0, N - 1):
                return 1

            if board[x][y] == WALL:
                continue

            for dx, dy in DELTA:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] != WALL:
                    visited[nx][ny] = True
                    new_moves.append((nx, ny))
        board.pop()
        board.insert(0, '.'*N)

        moves = new_moves
        if not moves:
            return 0


board = [stdin.readline().strip() for _ in range(8)]
print(solution(board))

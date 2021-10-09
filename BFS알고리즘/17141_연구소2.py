# 연구소 2

from collections import deque
from itertools import combinations

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(q, array, visited):
    global answer, cnt_1

    while q:
        now_x, now_y = q.popleft()
        for k in range(4):
            nx = now_x + dx[k]
            ny = now_y + dy[k]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1 and array[nx][ny] == 0:
                visited[nx][ny] = visited[now_x][now_y] + 1
                q.append((nx, ny))

    cnt_2 = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                cnt_2 += 1

    if cnt_2 != cnt_1:
        return -1

    max_n = 0
    for visit in visited:
        tmp = max(visit)
        if tmp > max_n:
            max_n = tmp

    return max_n


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


virus = []
cnt_1 = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            virus.append((i, j))
            board[i][j] = 0
        if board[i][j] == 1:
            cnt_1 += 1

answer = 2147000000

for comb in combinations(virus, m):
    q = deque()
    visited = [[-1] * n for _ in range(n)]
    max_num = 0
    for v in comb:
        q.append(v)
        visited[v[0]][v[1]] = 0
    max_num = bfs(q, board, visited)

    if max_num == -1:
        continue

    answer = min(answer, max_num)

if answer == 2147000000:
    answer = -1

print(answer)
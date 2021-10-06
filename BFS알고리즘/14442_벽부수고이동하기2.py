# 벽 부수고 이동하기 2


from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n, m, l = map(int, input().split())

board = [list(map(int, list(input()))) for _ in range(n)]

dist = [[[0]*(l+1) for j in range(m)] for i in range(n)]

q = deque()
q.append((0, 0, 0))
dist[0][0][0] = 1
while q:
    x, y, z = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<m:
            # 벽을 부수지 않은 경우
            if board[nx][ny] == 0 and dist[nx][ny][z] == 0:
                dist[nx][ny][z] = dist[x][y][z] + 1
                q.append((nx, ny, z))
            # 벽을 부수는 경우
            if z+1 <= l and board[nx][ny] == 1 and dist[nx][ny][z+1] == 0:
                dist[nx][ny][z+1] = dist[x][y][z] + 1
                q.append((nx, ny, z+1))

ans = -1
for i in range(l+1):
    if dist[n-1][m-1][i] == 0:
        continue
    if ans == -1:
        ans = dist[n-1][m-1][i]
    elif ans > dist[n-1][m-1][i]:
        ans = dist[n-1][m-1][i]
print(ans)

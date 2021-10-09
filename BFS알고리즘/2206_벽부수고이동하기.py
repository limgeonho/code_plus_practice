# 벽 부수고 이동하기
# 기본적인 bfs + 벽을 부술 수 있는 여부추가 => 난이도 상승
# 처음에는 bfs와 벽을 부술 수 있는 모든 경우를 구해서(브루트포스) 확인 => 시간초과
# bfs에서 경우를 나누는 경우 3차원 리스트로 0, 1 상태를 추가해서 기록!
from collections import deque
import pprint
dx = [0,0,1,-1]
dy = [1,-1,0,0]

n, m = map(int, input().split())
# 숫자로 들어온 값들을 리스트에 넣는 방법(split()한 효과)
board = [list(map(int, list(input()))) for _ in range(n)]
dist = [[[0]*2 for j in range(m)] for i in range(n)]

q = deque()
q.append((0, 0, 0))
dist[0][0][0] = 1
while q:
    x, y, z = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny] == 0 and dist[nx][ny][z] == 0:
                dist[nx][ny][z] = dist[x][y][z] + 1
                q.append((nx, ny, z))
            if z == 0 and board[nx][ny] == 1 and dist[nx][ny][z+1] == 0:
                dist[nx][ny][z+1] = dist[x][y][z] + 1
                q.append((nx, ny, z+1))

pprint.pprint(dist)

if dist[n-1][m-1][0] != 0 and dist[n-1][m-1][1] != 0:
    print(min(dist[n-1][m-1]))
elif dist[n-1][m-1][0] != 0:
    print(dist[n-1][m-1][0])
elif dist[n-1][m-1][1] != 0:
    print(dist[n-1][m-1][1])
else:
    print(-1)
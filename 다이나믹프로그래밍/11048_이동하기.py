# 이동하기

n, m = map(int,input().split())

board = [[0] * (m+1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

visited = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        visited[i][j] = max(visited[i-1][j], visited[i][j-1], visited[i-1][j-1]) + board[i][j]

print(visited[n][m])
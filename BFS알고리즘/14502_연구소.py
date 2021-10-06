# 연구소
# 각각의 벽을 세울 수 있는 경우를 전부 고려해야한다 => 브루트포스
# 브루트포스? => 전체 경우(6중 for 문)를 확인하면서 bfs순회

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(a):
    n = len(a)
    m = len(a[0])
    b = [[0] * m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            b[i][j] = a[i][j]
            if b[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m and b[nx][ny] == 0:
                b[nx][ny] = 2
                q.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if b[i][j] == 0:
                cnt += 1

    return cnt


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
# ==============================================
for x1 in range(n):
    for y1 in range(m):
        if board[x1][y1] != 0:
            continue
        for x2 in range(n):
            for y2 in range(m):
                if board[x2][y2] != 0:
                    continue
                for x3 in range(n):
                    for y3 in range(m):
                        if board[x3][y3] != 0:
                            continue
# ==============================================
                        # 고른 점들 중에 중복된 점들이 있다면 continue
                        if x1 == x2 and y1 == y2:
                            continue
                        if x1 == x3 and y1 == y3:
                            continue
                        if x2 == x3 and y2 == y3:
                            continue

                        # 선택확정하였다면 board에서 벽으로 설정
                        board[x1][y1] = 1
                        board[x2][y2] = 1
                        board[x3][y3] = 1

                        cur = bfs(board)

                        if answer < cur:
                            answer = cur

                        # bfs 순회 후 다시 0으로 원상태로 돌려놓음
                        # 브루트포스 : 준비 호출 되돌리기기
                        board[x1][y1] = 0
                        board[x2][y2] = 0
                        board[x3][y3] = 0

print(answer)
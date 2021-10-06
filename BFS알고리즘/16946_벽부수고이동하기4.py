# 벽 부수고 이동하기 4
# 변화하지 않는 부분이 계속 반복되면 저장해 놓고 활용하는 방법 생각


# 시간초과...
# from collections import deque
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
#
# def bfs(x, y, board):
#     array = board[:]
#     visited = [[False]*len(array[0]) for _ in range(len(array))]
#     q = deque()
#     q.append((x, y))
#     visited[x][y] = True
#     cnt = 0
#     while q:
#         now_x, now_y = q.popleft()
#         for k in range(4):
#             nx = now_x + dx[k]
#             ny = now_y + dy[k]
#             if 0<=nx<n and 0<=ny<m and array[nx][ny] == 0 and not visited[nx][ny]:
#                 visited[nx][ny] = True
#                 q.append((nx, ny))
#                 cnt += 1
#
#     return cnt
#
# n, m = map(int, input().split())
#
# board = [list(map(int, list(input()))) for _ in range(n)]
# answer = [[0]*m for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         if board[i][j] == 1:
#             board[i][j] = 0
#             answer[i][j] = bfs(i, j, board) + 1
#             board[i][j] = 1
#         else:
#             continue
#
# for arr in answer:
#     print(''.join(list(map(str, arr))))

# =================================================================

from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]

# 0으로 연결된 위치를 연결해서 grouping
group = [[-1]*m for _ in range(n)]

# 방문 여부 파악
check = [[False]*m for _ in range(n)]

# grouping한 것들의 크기를 저장
group_size = []


def bfs(sx, sy):
    # group[][]에 group번호로 저장된 것을 group_size[]로 접근해서 해당 grouping사이즈가 얼마인지 파악
    g = len(group_size)
    q = deque()
    q.append((sx, sy))
    group[sx][sy] = g
    check[sx][sy] = True
    cnt = 1
    while q:
        x, y, = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<m:
                if check[nx][ny] == False and a[nx][ny] == 0:
                    check[nx][ny] = True
                    group[nx][ny] = g
                    q.append((nx, ny))
                    cnt += 1
    group_size.append(cnt)


# 0으로 연결된 곳을 전부 bfs탐색해서 연결
for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and check[i][j] == False:
            bfs(i, j)


for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print(0, end='')
        else:
            near = set()
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<n and 0<=ny<m:
                    if a[nx][ny] == 0:
                        near.add(group[nx][ny])
            ans = 1

            for g in near:
                ans += group_size[g]
            print(ans%10, end='')
    print()

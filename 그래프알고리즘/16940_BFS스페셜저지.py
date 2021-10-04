# BFS 스페셜 저지

def dfs(x, answer):
    visited[x] = True
    answer.append(x)
    for nxt in board[x]:
        if not visited[nxt]:
            dfs(nxt, answer)

    return answer

n = int(input())
board = [[] * (n+1) for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

order = list(map(int, input().split()))

# 사용자로부터 받은 순서를 기준으로 연결리스트의 순서를 재정렬하고 BFS탐색한다.
rank = [-1 for i in range(n+1)]

for i in range(1, n+1):
    rank[order[i-1]] = i

for i in range(1, n+1):
    board[i] = sorted(board[i], key=lambda x: rank[x])
# =======================================================================

visited = [False] * (n+1)
stack = []

stack.append(1)
answer = []
visited[1] = True

dfs(1, answer)

if answer == order:
    print(1)
else:
    print(0)


# 뱀과 사다리 게임

from collections import deque

def bfs(start):
    q = deque()
    dist[start] = 0
    q.append(start)
    while q:
        now = q.popleft()
        # for문 이후가 한 덩어리의 큐들...(가중치가 +1 for문에 따라)
        for i in range(1, 7):
            nx = now + i
            if nx > 100:
                continue
            # 뱀과 사다리를 이용해서 변환되는 부분
            nx = nxt[nx]
            if dist[nx] == -1:
                dist[nx] = dist[now] + 1
                q.append(nx)


n, m = map(int, input().split())

# 일반적으로 거리는 양수이기 때문에 초기값을 -1로 설정
dist = [-1] * 101
nxt = list(range(101))

for _ in range(n+m):
    x, y = map(int, input().split())
    nxt[x] = y

bfs(1)

print(dist[100])


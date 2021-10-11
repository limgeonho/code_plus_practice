# 점프 점프

n = int(input())

array = list(map(int, input().split()))

answer = [99999999] * (4000)
answer[0] = 0
for i in range(len(array)):
    for j in range(1, array[i]+1):
        if answer[i+j] > answer[i] + 1:
            answer[i + j] = answer[i] + 1


if answer[n-1] != 99999999:
    print(answer[n-1])
else:
    print(-1)


# ===================================================

n = int(input())
lst = list(map(int, input().split()))

dp = [-1] * n

def bfs(start):
    q = []
    q.append(start)
    dp[start] = 0
    while q:
        now = q.pop(0)
        jump = lst[now]
        for i in range(jump, 0, -1):
            if now + i < n and dp[now + i] == -1:
                dp[now + i] = dp[now] + 1
                q.append(now + i)

bfs(0)
print(dp[-1])
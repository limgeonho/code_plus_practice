# 평범한 배낭

n, limit = map(int, input().split())

dp = [0] * (limit+1)

for _ in range(n):
    w, v = map(int, input().split())
    for i in range(limit, w-1, -1):
        dp[i] = max(dp[i], dp[i-w] + v)

print(max(dp))
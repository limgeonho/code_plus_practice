# 1학년
# 기타리스트와 매우 비슷한 문제

n = int(input()) - 1
array = list(map(int, input().split()))
goal = array[-1]
calc = array[:-1]

dp = [[0] * 21 for _ in range(n)]
dp[0][calc[0]] = 1

for i in range(1, n):
    for j in range(21):
        if j - calc[i] >= 0:
            dp[i][j] += dp[i-1][j - calc[i]]
        if j + calc[i] <= 20:
            dp[i][j] += dp[i-1][j + calc[i]]

print(dp[n-1][goal])

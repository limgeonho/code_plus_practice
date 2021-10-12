# LCS 4
# 메모리 초과...
length = int(input())

word_1 = list(map(str, input().split()))
word_2 = list(map(str, input().split()))

n = len(word_1)
m = len(word_2)

word_1 = [' '] + word_1
word_2 = [' '] + word_2


dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if word_1[i] == word_2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])
# 공통 부분 문자열

word_1 = input()
word_2 = input()
n = len(word_1)
m = len(word_2)

dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if word_1[i-1] == word_2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = 0

answer = 0
for row in dp:
    answer = max(answer, max(row))

print(answer)
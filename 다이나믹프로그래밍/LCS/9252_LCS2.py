# LCS2

w_1 = input()
w_2 = input()

n = len(w_1)
m = len(w_2)

w_1 = ' ' + w_1
w_2 = ' ' + w_2

dp = [[0] * (m+1) for _ in range(n+1)]
order = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if w_1[i] == w_2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            order[i][j] = 1
        else:
            if dp[i][j-1] > dp[i-1][j]:
                dp[i][j] = dp[i][j-1]
                order[i][j] = 2
            else:
                dp[i][j] = dp[i-1][j]
                order[i][j] = 3

print(dp[n][m])

answer = ''
while n>0 and m>0:
    if order[n][m] == 1:
        answer += w_1[n]
        n-=1
        m-=1
    elif order[n][m] == 2:
        m-=1
    else:
        n-=1

print(answer[::-1])



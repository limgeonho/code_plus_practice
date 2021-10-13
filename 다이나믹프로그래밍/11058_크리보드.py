# 크리보드

n = int(input())
d = [0] * (n+1)
for i in range(1,n+1):
    d[i] = d[i-1] + 1
    for j in range(1, i-3+1):
        cur = d[i-j-2]*(j+1)
        if cur > d[i]:
            d[i] = cur
print(d[n])
# 동전 1

n,m = map(int,input().split())
a = [int(input()) for _ in range(n)]
d = [0] * (m+1)
d[0] = 1
for i in range(n):
    for j in range(m+1):
        if j-a[i] >= 0:
            d[j] += d[j-a[i]]
print(d[m])

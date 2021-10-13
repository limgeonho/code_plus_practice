# 동전 2

n,m = map(int,input().split())
a = [int(input()) for _ in range(n)]
d = [-1] * (m+1)
d[0] = 0
for i in range(n):
    for j in range(m+1):
        if j-a[i] >= 0 and d[j-a[i]] != -1:
            if d[j] == -1 or d[j] > d[j-a[i]]+1:
                d[j] = d[j-a[i]] + 1
print(d[m])

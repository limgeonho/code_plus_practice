# 부분수열의 합

from itertools import combinations

n, s = map(int, input().split())

array = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    for j in combinations(array, i):
        if sum(j) == s:
            cnt += 1

print(cnt)

#######################################
def go(i, s):
    global ans
    if i == n:
        if s == m:
            ans += 1
        return
    go(i+1,s+a[i])
    go(i+1,s)

n,m = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
go(0, 0)
if m == 0:
    ans -= 1
print(ans)
# 기타리스트
import pprint
n,s,m = map(int,input().split())

a = list(map(int,input().split()))

d = [[False]*(m+1) for _ in range(n+1)]

d[0][s] = True

# dp는 이전의 값을 이용해서 다음에 올 값을 정하는 과정이 있어야함
# 이전에 True로 표시한 부분을 이용해서 다음 열의 True/False 여부를 판단한다.
for i in range(n):
    for j in range(m+1):
        if d[i][j] == False:
            continue
        if j-a[i] >= 0:
            d[i+1][j-a[i]] = True
        if j+a[i] <= m:
            d[i+1][j+a[i]] = True

ans = -1

for i in range(m+1):
    if d[n][i]:
        ans = i

# pprint.pprint(d)
print(ans)
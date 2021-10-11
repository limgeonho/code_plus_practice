# 파일 합치기

def go(i, j):
    if i == j:
        return 0
    if d[i][j] != -1:
        return d[i][j]
    ans = d[i][j]
    cost = sum(a[i:j+1])
    for k in range(i, j):
        temp = go(i,k) + go(k+1,j) + cost
        if ans == -1 or ans > temp:
            ans = temp
    d[i][j] = ans
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    d = [[-1]*n for _ in range(n)]
    print(go(0,n-1))

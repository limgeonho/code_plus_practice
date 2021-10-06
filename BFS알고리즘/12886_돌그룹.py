# 돌 그룹
# 최소값을 구하는 것이 아니고 단순하게 가능여부만 확인하기에 dfs
import sys
sys.setrecursionlimit(1500*1500)

def dfs(x, y):
    # 해당 숫자쌍이 나온적이 있는지
    if check[x][y]:
        return
    check[x][y] = True
    a = [x, y, total-x-y]
    # 모든 숫자쌍 확인하기
    for i in range(3):
        for j in range(3):
            if a[i] < a[j]:
                b = [x, y, total-x-y]
                b[i] += a[i]
                b[j] -= a[i]
                dfs(b[0], b[1])

a, b, c = map(int, input().split())

total = a + b + c

check = [[False]*1501 for _ in range(1501)]

# 총합이 3으로 나눠지지 않는 다면 골고루 분배할 수 없음
if total % 3 != 0:
    print(0)
else:
    # 돌은 두개만 알아도 나머지는 총합에서 1번째와 2번째를 각각 뺀 값임
    dfs(a, b)
    if check[total//3][total//3]:
        print(1)
    else:
        print(0)


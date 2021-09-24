# 로또

from itertools import combinations

while True:
    array = list(map(int, input().split()))
    if array[0] == 0:
        break
    for i in combinations(array[1:], 6):
        print(*i)
    print()



######################################################

def solve(a, index, lotto):
    if len(lotto) == 6:
        print(' '.join(map(str,lotto)))
        return
    if index == len(a):
        return
    solve(a, index+1, lotto+[a[index]])
    solve(a, index+1, lotto)

while True:
    n, *a = list(map(int,input().split()))
    if n == 0:
        break
    solve(a, 0, [])
    print()
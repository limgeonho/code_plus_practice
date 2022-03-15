# 로또

# from itertools import combinations
#
# while True:
#     array = list(map(int, input().split()))
#     if array[0] == 0:
#         break
#     for i in combinations(array[1:], 6):
#         print(*i)
#     print()
#


######################################################

# def solve(a, index, lotto):
#     if len(lotto) == 6:
#         print(' '.join(map(str,lotto)))
#         return
#     if index == len(a):
#         return
#     solve(a, index+1, lotto+[a[index]])
#     solve(a, index+1, lotto)
#
# while True:
#     n, *a = list(map(int,input().split()))
#     if n == 0:
#         break
#     solve(a, 0, [])
#     print()

def comb(L, start):
    if L == 6:
        print(*res)
        return
    for i in range(start, len(array)):
        res[L] = array[i]
        comb(L+1, i+1)

while True:
    array = list(map(int, input().split()))
    L = array[0]
    array = array[1:]
    if L == 0:
        break

    res = [0] * 6
    comb(0, 0)

    print()

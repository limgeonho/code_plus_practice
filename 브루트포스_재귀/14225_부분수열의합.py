# 부분수열의 합

# from itertools import combinations
#
# n = int(input())
# array = list(map(int, input().split()))
# tmp = set()
#
# for i in range(1, n+1):
#     for j in combinations(array, i):
#         tmp.add(sum(j))
#
# answer = 0
#
# for i in range(1, sum(array) + 2):
#     if i not in tmp:
#         answer = i
#         break
#
# print(answer)

##################################################
# n = int(input())
# a = list(map(int,input().split()))
# c = [False]*(n*100000+10)
# def go(i, sum):
#     if i == n:
#         c[sum] = True
#         return
#     go(i+1,sum+a[i])
#     go(i+1,sum)
# go(0,0)
# i = 1
# while True:
#     if c[i] == False:
#         break
#     i += 1
# print(i)


def subset(L, ss):
    if L == n:
        res[ss] = True
        return
    subset(L+1, ss)
    subset(L+1, ss + array[L])

n = int(input())
array = list(map(int, input().split()))

res = [False] *(n*100000+10)

subset(0, 0)
i = 1
while True:
    if not res[i]:
        break
    i += 1

print(i)
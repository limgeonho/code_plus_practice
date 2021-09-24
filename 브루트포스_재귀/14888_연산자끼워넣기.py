# 연산자 끼워넣기

from itertools import permutations

check = {0: '+', 1: '-', 2: '*', 3: '//'}

n = int(input())
array = list(map(str, input().split()))
operators = list(map(int, input().split()))

tmp = []
for i in range(len(operators)):
    for j in range(operators[i]):
        tmp.append(i)
answer = []
for i in permutations(tmp):
    array_1 = array[:]
    tmp = list(i)
    stack = ''
    stack += array_1.pop()
    while True:
        stack += check[tmp.pop()]
        stack += array_1.pop()
        stack = eval(stack)

    print(stack)
print(answer)



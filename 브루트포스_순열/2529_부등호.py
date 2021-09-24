# 부등호

from itertools import permutations

n = int(input())
array = list(map(str, input().split())) + ['']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
answer = []
final = []
for i in permutations(numbers, n+1):
    i = list(i)
    tmp = []
    for j in range(n+1):
        tmp.append(i[j])
        tmp.append(array[j])
    candidate = ''.join(tmp[:-1])
    if eval(candidate):
        answer.append(candidate)
for i in answer:
    tmp = ''
    for j in range(len(i)):
        if i[j].isdigit():
           tmp += i[j]
    final.append(tmp)

print(int(final[-1]))
print(int(final[0]))
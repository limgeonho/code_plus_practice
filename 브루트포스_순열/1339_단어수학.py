# 단어 수학

# def next_permutation(a):
#     i = len(a)-1
#     while i > 0 and a[i-1] >= a[i]:
#         i -= 1
#     if i <= 0:
#         return False
#     j = len(a)-1
#     while a[j] <= a[i-1]:
#         j -= 1
#
#     a[i-1],a[j] = a[j],a[i-1]
#
#     j = len(a)-1
#     while i < j:
#         a[i],a[j] = a[j],a[i]
#         i += 1
#         j -= 1
#
#     return True
#
# def calc(a, letters, d):
#     m = len(letters)
#     ans = 0
#     alpha = dict()
#     for i in range(m):
#         alpha[letters[i]] = d[i]
#     for s in a:
#         now = 0
#         for x in s:
#             now = now * 10 + alpha[x]
#         ans += now
#     return ans
# n = int(input())
# a = ['']*n
# letters = set()
# for i in range(n):
#     a[i] = input()
#     letters |= set(a[i])
# letters = list(letters)
# m = len(letters)
# d = [i for i in range(9, 9-m, -1)]
# d.sort()
# ans = 0
# while True:
#     now = calc(a, letters, d)
#     if ans < now:
#         ans = now
#     if not next_permutation(d):
#         break
# print(ans)

import sys


n = int(sys.stdin.readline())
alphabet_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
alphabet_list = []
answer = 0
pocket = []

for _ in range(n):
    alphabet = input()
    pocket.append(alphabet)

for alphabet in pocket:
    for i in range(len(alphabet)):
        num = 10**(len(alphabet)-i-1)
        alphabet_dict[alphabet[i]] += num

for value in alphabet_dict.values():
    if value > 0:
        alphabet_list.append(value)

sorted_list = sorted(alphabet_list, reverse=True)
for i in range(len(sorted_list)):
    answer += sorted_list[i] * (9-i)

print(answer)
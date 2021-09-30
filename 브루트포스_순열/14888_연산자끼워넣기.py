# 연산자 끼워넣기


def next_permutation(array):
    i = len(array) - 1
    while i > 0 and array[i-1] >= array[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(array) - 1
    while array[j] <= array[i-1]:
        j -= 1
    array[i-1], array[j] = array[j], array[i-1]

    j = len(array) - 1
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    return True


def div(a, b):
    if a >= 0:
        return a // b
    else:
        return -(-a // b)


def calc(a, b):
    n = len(a)
    ans = a[0]
    for i in range(1, n):
        if b[i-1] == 0:
            ans = ans + a[i]
        elif b[i - 1] == 1:
            ans = ans - a[i]
        elif b[i - 1] == 2:
            ans = ans * a[i]
        else:
            ans = div(ans, a[i])
    return ans


n = int(input())
a = list(map(int, input().split()))
cnts = list(map(int, input().split()))
b = []
for i, cnt in enumerate(cnts):
    for k in range(cnt):
        b.append(i)
b.sort()
answer = []

while True:
    tmp = calc(a, b)
    answer.append(tmp)
    if not next_permutation(b):
        break

answer.sort()
print(max(answer))
print(min(answer))
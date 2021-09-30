# 부등호

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


def prev_permutation(array):
    i = len(array) - 1
    while i > 0 and array[i - 1] <= array[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(array) - 1
    while array[j] >= array[i - 1]:
        j -= 1
    array[i - 1], array[j] = array[j], array[i - 1]

    j = len(array) - 1
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1
    return True


def check(perm, array):
    for i in range(len(array)):
        if array[i] == '<' and perm[i] > perm[i+1]:
            return False
        if array[i] == '>' and perm[i] < perm[i + 1]:
            return False
    return True

k = int(input())
array = input().split()
small = [i for i in range(k+1)]
big = [9-i for i in range(k+1)]

while True:
    if check(small, array):
        break
    if not next_permutation(small):
        break

while True:
    if check(big, array):
        break
    if not prev_permutation(big):
        break

print(''.join(map(str, big)))
print(''.join(map(str, small)))
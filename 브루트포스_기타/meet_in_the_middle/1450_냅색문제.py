# 냅색문제
# meet in the middle
# binary search

def check_a(level, weight):
    if level == len(a_array):
        a_total.append(weight)
        return
    check_a(level+1, weight)
    check_a(level+1, weight + a_array[level])


def check_b(level, weight):
    if level == len(b_array):
        b_total.append(weight)
        return
    check_b(level+1, weight)
    check_b(level+1, weight + b_array[level])

def search(arr, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return end


n, c = map(int, input().split())
array = list(map(int, input().split()))

a_array = array[:n//2]
b_array = array[n//2:]

a_total = []
b_total = []

check_a(0, 0)
check_b(0, 0)

a_total.sort()
b_total.sort()

cnt = 0
for num in a_total:
    if c - num < 0:
        continue
    cnt += search(b_total, c-num, 0, len(b_total))
print(cnt)

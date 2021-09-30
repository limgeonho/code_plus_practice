# 부분합


n, s = map(int, input().split())
a = list(map(int, input().split()))

left = right = 0
sum = a[0]
answer = n+1

while left <= right and right < n:
    if sum < s:
        right += 1
        if right < n:
            sum += a[right]
    elif sum == s:
        answer = min(right-left +1, answer)
        right += 1
        if right < n:
            sum += a[right]
    elif sum > s:
        answer = min(right - left + 1, answer)
        sum -= a[left]
        left += 1
        if left > right and left < n:
            right = left
            sum = a[left]

if answer > n:
    answer = 0

print(answer)
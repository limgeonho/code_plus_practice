# 수들의 합2
# 투 포인터

n, m = map(int, input().split())
array = list(map(int, input().split()))

interval = 0
cnt = 0
end = 0
for start in range(n):
    while interval < m and end < n:
        interval += array[end]
        end += 1

    if interval == m:
        cnt += 1

    interval -= array[start]

print(cnt)
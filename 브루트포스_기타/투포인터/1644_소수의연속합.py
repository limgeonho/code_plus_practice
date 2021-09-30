# 소수의 연속합

n = int(input())

prime_nums = [True] * (n+1)
array = []

for i in range(2, int(n**0.5)+1):
    if prime_nums[i] == True:
        j = 2
        while i*j <= n:
            prime_nums[i*j] = False
            j += 1


for i in range(2, n+1):
    if prime_nums[i]:
        array.append(i)

interval = 0
cnt = 0
end = 0

for start in range(len(array)):
    while end < len(array) and interval < n:
        interval += array[end]
        end += 1
    if interval == n:
        cnt += 1
    interval -= array[start]

print(cnt)

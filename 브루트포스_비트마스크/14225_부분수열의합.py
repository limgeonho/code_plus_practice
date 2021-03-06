# 부분수열의 합
# 부분집합을 다루는 문제에서는 비트마스크를 생각해보자

n = int(input())
array = list(map(int, input().split()))
check = [False] * 2000000

# 2**n => 나올 수 있는 전체 경우의 수
for i in range(1<<n):
    # 하나의 경우의 수마다 total값 리셋
    total = 0
    # array의 원소의 개수만큼 순회 => 해당 인덱스의 원소가 경우의 수에 존재하는지 파악
    for j in range(n): # n = (0, 1, 2)
        # 경우의 수(10진수로 표현해 놓은 것)에 0,1,2에 해당하는 인덱스의 원소가 존재하는지 여부 파악
        if (i & (1<<j)):
            # i => 0 ~ 7
            # 1<<j => 0 ~ 2
            # (i & (1<<j)) => i안에 (1<<j)가 존재한다면 True
            # True인 경우 해당 인덱스의 array값을 total에 누적
            total += array[j]
    check[total] = True

i = 1
while True:
    if check[i] == False:
        break
    i += 1
print(i)
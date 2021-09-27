# 에너지 모으기
0
def go(array):
    n = len(array)
    if n == 2:
        return 0

    answer = 0
    for i in range(1, n-1):
        energy = array[i-1] * array[i+1]
        b = array[:i] + array[i+1:]
        energy += go(b)
        if answer < energy:
            answer = energy
    return answer

n = int(input())
array = list(map(int, input().split()))
print(go(array))
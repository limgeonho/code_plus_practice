# 연산자 끼워넣기


def calc(array, index, cur, plus, minus, mul, div):
    if index == len(array):
        return (cur, cur)
    res = []

    if plus > 0:
        res.append(calc(array, index+1, cur+array[index], plus-1, minus, mul, div))
    if minus > 0:
        res.append(calc(array, index+1, cur-array[index], plus, minus-1, mul, div))
    if mul > 0:
        res.append(calc(array, index+1, cur*array[index], plus, minus, mul-1, div))
    if div > 0:
        if cur >= 0:
            res.append(calc(array, index+1, cur//array[index], plus, minus, mul, div-1))
        else:
            res.append(calc(array, index + 1, -(-cur // array[index]), plus, minus, mul, div - 1))
    ans = (
        max([t[0] for t in res]),
        min([t[1] for t in res])
    )
    print(ans)
    return ans

n = int(input())
array = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
# calc([3,4,5], 1, [3], 1, 0, 1, 0)
answer = calc(array, 1, array[0], plus, minus, mul, div)
print(answer[0])
print(answer[1])
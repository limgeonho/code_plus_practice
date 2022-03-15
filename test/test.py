import sys

sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    place = []
    cnt = 0
    array = [0] * (n+1)
    for _ in range(3):
        place.append(list(map(int, input().split())))
    place.sort()
    tmp1 = place[0][0] - 1
    tmp2 = n - place[2][0]

    if tmp1 > tmp2:
        start = place[2][0]
    else:
        start = place[0][0]

    for pl in place:

        for i in range(1, pl[1] + 1):
            while True:
                tmp4 = 0
                tmp_l = 0
                tmp_r = 0
                if array[pl[0] + tmp4]:
                    array[pl[0]] = tmp4+1
                    tmp_l = tmp4 -1
                    tmp_r = tmp4 +1
                    tmp4 += 1

                else:
                    if array[pl[0] + tmp_r]:
                        array[pl[0] + tmp_r] = tmp4 +1
                        tmp_r += 1
                    else:

                        array[pl[0] + tmp_l] = tmp4 + 1
                        tmp_l -= 1


    print(array)


    print("=================")

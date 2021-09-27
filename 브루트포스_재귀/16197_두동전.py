# 두 동전


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def go(step, x1, y1, x2, y2):
    if step == 11:
        return -1

    fall1 = False
    fall2 = False

    if x1 < 0 or x1 >= n or y1 < 0 or y1 >= m:
        fall1 = True
    if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m:
        fall2 = True

    if fall1 and fall2:
        return -1
    if fall1 or fall2:
        return step

    answer = -1

    for k in range(4):
        nx1, ny1 = x1 + dx[k], y1 + dy[k]
        nx2, ny2 = x2 + dx[k], y2 + dy[k]
        if 0 <= nx1 < n and 0 <= ny1 < m and array[nx1][ny1] == '#':
            nx1, ny1 = x1, y1
        if 0 <= nx2 < n and 0 <= ny2 < m and array[nx2][ny2] == '#':
            nx2, ny2 = x2, y2

        tmp = go(step+1, nx1, ny1, nx2, ny2)
        if tmp == -1:
            continue
        if answer == -1 or answer > tmp:
            answer = tmp

    return answer


n, m = map(int, input().split())
array = [list(input()) for _ in range(n)]
x1 = x2 = y1 = y2 = -1

for i in range(n):
    for j in range(m):
        if array[i][j] == 'o':
            if x1 == -1:
                x1, y1 = i, j
            else:
                x2, y2 = i, j
            array[i][j] = '.'

print(go(0, x1, y1, x2, y2))
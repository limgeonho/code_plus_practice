# 스도쿠


def square(x, y):
    return (x//3)*3 + (y//3)

def go(z):
    if z == 81:
        for row in array:
            print(' '.join(map(str, row)))
        return True
    x = z // n
    y = z % n
    if array[x][y] != 0:
        return go(z+1)
    else:
        for i in range(1, 10):
            if c1[x][i] == False and c2[y][i] == False and c3[square(x, y)][i] == False:
                c1[x][i] = c2[y][i] = c3[square(x, y)][i] = True
                array[x][y] = i
                if go(z+1):
                    return True
                array[x][y] = 0
                c1[x][i] = c2[y][i] = c3[square(x, y)][i] = False
    return False

n = 9
array = [list(map(int, input().split())) for _ in range(n)]
c1 = [[False]*10 for _ in range(n)] # 행 점검
c2 = [[False]*10 for _ in range(n)] # 열 점검
c3 = [[False]*10 for _ in range(n)] # 3*3사각형 점검

for i in range(n):
    for j in range(n):
        # 해당 위치에 0이 있는지 파악
        if array[i][j] != 0:
            # 없다면 행, 열, 사각형 점검리스트에 표시
            c1[i][array[i][j]] = True
            c2[j][array[i][j]] = True
            c3[square(i,j)][array[i][j]] = True

go(0)
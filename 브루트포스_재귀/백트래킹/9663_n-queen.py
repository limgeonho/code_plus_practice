# n-queen

# def is_available(candidate, current_col):
#     current_row = len(candidate)
#     for queen_row in range(current_row):
#         if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
#             return False
#     return True
#
# def queen(n, current_row, current_candidate):
#     global final_cnt
#     if current_row == n:
#         # final.append(current_candidate[:])
#         final_cnt += 1
#         return
#
#     for candidate_col in range(n):
#         if is_available(current_candidate, candidate_col):
#             current_candidate.append(candidate_col)
#             queen(n, current_row+1, current_candidate)
#             current_candidate.pop()
#
# n = int(input())
# final = []
# final_cnt = 0
# queen(n, 0, [])
# print(final_cnt)
# # print(len(final))



def available(current_col, candidate):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

def DFS(n, current_row, current_candidate):
    global cnt
    if current_row == n:
        cnt += 1
        return

    for candidate_col in range(n):
        if available(candidate_col, current_candidate):
            current_candidate.append(candidate_col)
            DFS(n, current_row+1, current_candidate)
            current_candidate.pop()

n = int(input())
cnt = 0
DFS(n, 0, [])
print(cnt)

#########################################################################################

def check(row, col):
    if check_col[col]:
        return False
    if check_dig[row+col]:
        return False
    if check_dig2[row-col+n-1]:
        return False
    return True

def calc(row):
    if row == n:
        return 1
    ans = 0
    for col in range(n):
        if check(row,col):
            check_dig[row+col] = True
            check_dig2[row-col+n-1] = True
            check_col[col] = True
            a[row][col] = True
            ans += calc(row+1)
            check_dig[row+col] = False
            check_dig2[row-col+n-1] = False
            check_col[col] = False
            a[row][col] = False
    return ans

n = int(input())
a = [[False]*n for _ in range(n)]
check_col = [False] * n
check_dig = [False] * (2*n-1)
check_dig2 = [False] * (2*n-1)
print(calc(0))

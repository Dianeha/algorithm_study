import sys
sys.stdin = open("치즈.txt", "r")

sero, garo = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(sero)]

# 구멍 위 왼 아래 오
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):

    if not (0 <= x < sero and 0 <= y < garo): return
    if pan[x][y]: return

    pan[x][y] = 9

    for i in range(4):
        dfs(x + dx[i], y + dy[i])

cnt = 0
cheese = 0
flag = True
while flag:
    cnt += 1
    for i in range(sero):
        for j in range(garo):
            dfs(0, 0)

    for i in range(sero):
        print(pan[i], end='\n')

    for i in range(sero):
        for j in range(garo):
            if pan[i][j] == 1:
                if pan[i+1][j] == 9 or pan[i-1][j] == 9 or pan[i][j+1] == 9 or pan[i][j-1] == 9:
                    pan[i][j] = 9
                else:
                    cheese += 1
    if cheese == 0:
        flag = False

print(cnt)








# for i in range(sero):
#     for j in range(garo):
#         if pan[i][j]== 2:
#             pan[i][j] = 0
#         if pan[i][j]== 1 and (pan[i+1][j] == 0 or pan[i-1][j] == 0 or pan[i][j+1] == 0 or pan[i][j-1] == 0):
# #             pan[i][j] = 2



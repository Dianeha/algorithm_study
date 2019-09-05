import sys
sys.stdin = open("test.txt", "r")

sero, garo = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(sero)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):

    if not (0 <= x < sero and 0 <= y < garo): return
    if pan[x][y]: return

    pan[x][y] = 9

    for i in range(4):
        dfs(x + dx[i], y + dy[i])

cnt = 0
flag = True
howManyCheese = [0] * 100
n = 0
for i in range(sero):
    for j in range(garo):
        if pan[i][j] == 1:
            n += 1
# print('처음치즈 {}개'.format(n))

while True:
    cnt += 1
    # print(cnt)
    cheese = 0
    dfs(0, 0)

    for i in range(sero):
        for j in range(garo):
            if pan[i][j] == 1:
                if pan[i+1][j] == 9 or pan[i-1][j] == 9 or pan[i][j+1] == 9 or pan[i][j-1] == 9:
                    pan[i][j] = 0
                else:
                    cheese += 1

    # for i in range(sero):
    #     for j in range(garo):
    #         print(pan[i][j], end=' ')
    #         if j == garo-1:
    #             print()
    # print()

    howManyCheese[cnt] = cheese
    if cheese == 0:
        break

    for i in range(sero):
        for j in range(garo):
            if pan[i][j] == 9:
                pan[i][j] = 0

    # for i in range(sero):
    #     for j in range(garo):
    #         print(pan[i][j], end=' ')
    #         if j == garo-1:
    #             print()
    # print(howManyCheese[:cnt+1])


print(cnt)
print(howManyCheese[cnt-1])
import sys
sys.stdin = open("ladder1.txt", "r")

def isWall(x, y):
    if y < 0 or y >= 100:
        return False
    elif ladder[x][y] == 0:
        return False
    else:
        return True

def checkLeft(X, Y):
    global dir_stat
    if ladder[X][Y - 1]:  # 왼
        dir_stat = 2
        while isWall(X, Y):
            X = X + dx[dir_stat]
            Y = Y + dy[dir_stat]
        X -= dx[dir_stat]
        Y -= dy[dir_stat]
        dir_stat = 0
        return X, Y
    else:
        pass

def checkRight(X, Y):
    global dir_stat
    if ladder[X][Y + 1]:  # 오
        dir_stat = 1
        while isWall(X, Y):
            X = X + dx[dir_stat]
            Y = Y + dy[dir_stat]
        X -= dx[dir_stat]
        Y -= dy[dir_stat]
        dir_stat = 0
        return X, Y
    else:
        pass

for _ in range(1, 11):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    ending = 0
    for i in range(100):
        if ladder[-1][i] == 2:
            ending = i

    X = 99
    Y = ending
    dx = [-1, 0, 0]
    dy = [0, 1, -1]
    dir_stat = 0  # 0:위, 1:오, 2:왼

    while X != 0:

        X = X + dx[dir_stat]
        Y = Y + dy[dir_stat]

        if Y==0:
            res = checkRight(X, Y)
        elif Y == 99:
            res = checkLeft(X, Y)
        else:
            res = checkRight(X, Y)
            res = checkLeft(X, Y)

        if res:
            res[0] = X
            res[1] = Y




        # if isWall(X, Y):
        #     X -= dx[dir_stat]
        #     Y -= dy[dir_stat]
        #     if ladder[X][Y-1]: # 왼쪽
        #         dir_stat = 2
        #     elif ladder[X][Y+1]: # 오른쪽
        #         dir_stat = 1
        #     elif ladder[X-1][Y] == 1: # 위
        #         dir_stat = 0

    print('#{} {} {}'.format(tc, ending, Y))

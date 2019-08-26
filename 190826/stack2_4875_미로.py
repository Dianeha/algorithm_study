import sys
sys.stdin = open("input_stack2_4875.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def findStart(mazeArray):
    xy = [0, 0]
    for i in range(n):
        for j in range(n):
            if mazeArray[i][j] == 2:
                xy[0] = i
                print(i)
                xy[1] = j
                print(j)
                return xy

def dfs(x, y):
    if not (0 <= x < n and 0 <= y < n): return
    if mazeArray[x][y] == 3: return 1
    if mazeArray[x][y] == 1: return

    mazeArray[x][y] = 1

    for i in range(4):
        dfs(x + dx[i], y + dy[i])


for tc in range(1, int(input())+1):
    n = int(input())
    mazeArray = [[x for x in input()] for _ in range(n)]

    # while True:
    # s = findStart(mazeArray)
    print(findStart(mazeArray))
        # mazeArray[s[0]][s[1]] = 1
        # dfs(s[0], s[1])

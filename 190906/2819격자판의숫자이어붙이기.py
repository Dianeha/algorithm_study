import sys
sys.stdin = open("격자판.txt", "r")

positiveNums = set()
tempNum = ''
def dfsNum(x, y):
    global tempNum
    stackXY = [[x, y]]  # 0.0 에서 시작하는 것만 하는 중
    dx = [-1, 0, 1, 0] # 위 오른쪽 아래 왼쪽
    dy = [0, 1, 0, -1]
    tempNum += pan[x][y]
    while len(stackXY) != 0:
        now = stackXY.pop()
        for k in range(4):
            tempNum = tempNum[:-1]
            nX = now[0] + dx[k]
            nY = now[1] + dy[k]
            if 0 <= nX < 3 and 0 <= nY < 3:
                tempNum += pan[x][y]
                while len(tempNum) != 4:
                    stackXY.append([nX, nY])
                    dfsNum(nX, nY)
                    positiveNums.add(tempNum)

T = int(input())
for tc in range(1, T+1):
    pan = [input().split() for _ in range(3)]

    dfsNum(0, 0)

    print(positiveNums)
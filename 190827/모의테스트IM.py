import sys
sys.stdin = open("input_test.txt", "r")

def coloring(x1, y1, x2, y2, m):
    maxM = 0
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if matrix[x][y] > maxM:
                maxM = matrix[x][y]

    if maxM <= m:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                matrix[x][y] = m


for tc in range(1, int(input())+1):
    nmk = list(map(int, input().split()))
    N, M, K = nmk[0], nmk[1], nmk[2]
    matrix = [[0 for _ in range(M)] for _ in range(N)]

    mDict = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}

    for _ in range(K):
        d = list(map(int, input().split()))
        x1, y1, x2, y2, m = d[0], d[1], d[2], d[3], d[4]
        coloring(x1, y1, x2, y2, m)

    for i in range(N):
        for j in range(M):
            mDict[str(matrix[i][j])] += 1

    print('#{} {}'.format(tc, max(mDict.values())))



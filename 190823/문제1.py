T = int(input())
for tc in range(1, T+1):
    NM = list(map(int, input().split()))
    N = NM[0]
    M = NM[1]
    area = [[0]*N for _ in range(N)]

    for m in range(M):
        points = list(map(int, input().split()))
        x1, y1, x2, y2 = points[0], points[1], points[2], points[3]

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                area[x][y] = 1

    cnt = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] == 1:
                cnt += 1

    print('#{} {}'.format(tc, cnt))
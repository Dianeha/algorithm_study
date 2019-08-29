T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    row, col, k = data[0], data[1], data[2]

    area = [list(map(int, input().split())) for _ in range(row)]

    maxSum = 0
    for i in range(row-k+1):
        for j in range(col-k+1): # 사각형의 시작점

            # 큰 사각형의 합
            sum1 = 0
            for x in range(k):
                for y in range(k):
                    sum1 += area[i+x][j+y]

            # 작은 사각형의 합
            sum2 = 0
            for x in range(k-2):
                for y in range(k-2):
                    sum2 += area[i+1+x][j+1+y]

            res = sum1 - sum2
            if res > maxSum:
                maxSum = res

    print("#{} {}".format(tc, maxSum))

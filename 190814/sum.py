import sys
sys.stdin = open("sum.txt", "r")

for tc in range(1, 11):
    test_case = int(input())
    arr = []
    for row in range(100):
        arr.append(list(map(int, input().split())))

    # 가로합
    garo_max = 0
    for i in range(100):
        garo_sum = 0
        for j in range(100):
            garo_sum += arr[i][j]
        if garo_sum > garo_max:
            garo_max = garo_sum

    # 세로합
    sero_max = 0
    for i in range(100):
        sero_sum = 0
        for j in range(100):
            sero_sum += arr[j][i]
        if sero_sum > sero_max:
            sero_max = sero_sum

    # 대각선 합
    x1_sum = x2_sum = 0
    for i in range(100):
        x1_sum += arr[i][i]
        x2_sum += arr[i][99-i]

    nums = [garo_max, sero_max, x1_sum, x2_sum]
    real_max = garo_max
    for i in range(1, 4):
        if nums[i] > real_max:
            real_max = nums[i]

    print('#{} {}'.format(test_case, real_max))
import sys
sys.stdin = open("sum.txt", "r")

for tc in range(1, 11):
    test_case = int(input())
    arr = []
    for row in range(100):
        arr.append(list(map(int, input().split())))

    garo_max = sero_max = x1_sum = x2_sum = 0
    for i in range(100):
        garo_sum = 0
        sero_sum = 0
        x1_sum += arr[i][i]
        x2_sum += arr[i][99 - i]
        for j in range(100):
            garo_sum += arr[i][j]
            sero_sum += arr[j][i]

        if garo_sum > garo_max:
            garo_max = garo_sum

        if sero_sum > sero_max:
            sero_max = sero_sum

    print('#{} {}'.format(test_case, max(garo_max, sero_max, x1_sum, x2_sum)))

    # for x in range(10):
    #     n = int(input())
    #     a = []
    #     for _ in range(100):
    #         b = list(map(int, input().split()))
    #         a.append(b)
    #
    #     sum_list = []
    #
    #     for p in range(100):
    #         width = 0
    #         height = 0
    #         for q in range(100):
    #             width += a[p][q]
    #             height += a[q][p]
    #         sum_list.append(width)
    #         sum_list.append(height)
    #     chk = 0
    #     cross = 0
    #     for p in a:
    #         cross += p[chk]
    #         chk += 1
    #     sum_list.append(cross)
    #
    #     chk = -1
    #     cross = 0
    #     for p in a:
    #         cross += p[chk]
    #         chk -= 1
    #     sum_list.append(cross)
    #
    #     print('#{} {}'.format(n, max(sum_list)))
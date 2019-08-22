import sys
sys.stdin = open("input.txt", "r")

matrix = [list(map(int, input().split())) for i in range(5)]
nums = []
bingo = ['x'] * 5
for i in range(5):
    nums.extend(map(int, input().split()))

for num in nums:

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == num:
                matrix[i][j] = 'x'

    g, s, d, rd = 0, 0, 0, 0
    if nums.index(num) >= 4:
        for i in matrix:
            if i == bingo:
                g += 1

        cnt = 0
        for i in range(5):
            cnt = 0
            for j in range(5):
                if matrix[j][i] == 'x':
                    cnt += 1
            if cnt == 5:
                s += 1

        cnt = 0
        for i in range(5):
            if matrix[i][i] == 'x':
                cnt += 1
        if cnt == 5:
            d += 1

        cnt = 0
        for i in range(5):
            if matrix[i][4-i] == 'x':
                cnt += 1
        if cnt == 5:
            rd += 1

    bingo_cnt = g + s + d + rd
    if bingo_cnt >= 3:
        break


print(nums.index(num)+1)
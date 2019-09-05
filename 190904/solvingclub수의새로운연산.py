import sys
sys.stdin = open('input새로운연산.txt', 'r')

points = [[0, 0, 0]]  # 각 점마다 [숫자, x, y] 다 저장
k = 1
n = 1
while n <= 40000:
    for i in range(1, k+1):
        points += [[n, i, k+1-i]]
        n += 1
    k += 1

T = int(input())
for tc in range(1, T+1):
    p, q = map(int, input().split())

    resX = points[p][1] + points[q][1]
    resY = points[p][2] + points[q][2]

    for point in points:
        if point[1] == resX and point[2] == resY:
            print(f'#{tc} {point[0]}')
            break
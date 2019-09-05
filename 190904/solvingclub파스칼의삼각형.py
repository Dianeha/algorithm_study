import sys
sys.stdin = open('input파스칼의삼각형.txt', 'r')

# for tc in range(1, int(input())+1):
# #     N = int(input())
# #     print(f'#{tc}')
# #     resFront = [1]
# #     print(1)
# #     for i in range(1, N+1):
# #         if i == 1:
# #             continue
# #         resBack = []
# #         for j in range(i):
# #             if j == 0 or j == i-1:
# #                 resBack.append(1)
# #             else:
# #                 resBack.append(resFront[j-1]+resFront[j])
# #
# #         for k in range(len(resBack)):
# #             print(resBack[k], end=' ')
# #         print()
# #         resFront = resBack

# 지선이 풀이
def sol(N):
    H = [[0] * (i + 1) for i in range(N)]
    for i in range(N):
        for j in range(i + 1):
            if i == 0 or i == 1:
                H[i][j] = 1
            elif j == 0 or j == i:
                H[i][j] = 1
            else:
                H[i][j] = H[i - 1][j - 1] + H[i - 1][j]
    return H

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    res = sol(N)
    print('#{}'.format(tc))
    for i in range(N):
        print(' '.join(map(str, res[i])))
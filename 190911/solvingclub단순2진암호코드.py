import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    print(arr)
    # for i in range(N):
    #     for j in range(M-1, 0, -1):
    #         if arr[i][j]:
    #             codeLine = i
    #             codeStart = j
    #             break
    # print(codeLine, codeStart)
import sys
sys.stdin = open('input어디에단어.txt', 'r')

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    NN = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N-K+1):
            a = NN[i][j:j+K]
            if NN[i][j:j + K] == [1] * K:
                if j == 0 and NN[i][j+K] == 0:
                    cnt += 1
                elif j == N-K and NN[i][j-1] == 0:
                    cnt += 1
                elif 0 < j < N-K and NN[i][j-1] == 0 and NN[i][j+K] == 0:
                    cnt += 1

    for i in range(N - K + 1):
        for j in range(N):
            test = [0] * K
            for m in range(K):
                test[m] = NN[i+m][j]
            if test == [1] * K:
                if i == 0 and NN[i+K][j] == 0:
                    cnt += 1
                elif 0 < i < N-K and NN[i + K][j] == 0 and NN[i - 1][j] == 0:
                    cnt += 1
                elif i == N-K and NN[i-1][j] == 0:
                    cnt += 1
    print(f'#{tc} {cnt}')

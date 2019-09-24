import sys
sys.stdin = open('input5209.txt', 'r')

def findMin(k, val):
    global ans

    if k == N:
        if val < ans:
            ans = val
    else:
        for i in range(k, N):
            perm[k], perm[i] = perm[i], perm[k]
            if val + mat[k][perm[k]] < ans:
                findMin(k + 1, val + mat[k][perm[k]])
            perm[k], perm[i] = perm[i], perm[k]


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        ans += mat[i][i]
    perm = [x for x in range(N)]

    findMin(0, 0)
    print("#%d %d" % (tc, ans))
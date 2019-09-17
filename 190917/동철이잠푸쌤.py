import sys
sys.stdin = open('input.txt', 'r')

def solve(k, val):
    global ans
    global cnt
    cnt += 1
    if k == N:
        if val > ans:
            ans = val
    else:
        for i in range(k, N):
            perm[k], perm[i] = perm[i], perm[k]
            if val * mat[k][perm[k]] > ans:
                solve(k + 1, val * mat[k][perm[k]])
            perm[k], perm[i] = perm[i], perm[k]


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    mat = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]

    cnt = 0
    ans = 1
    for i in range(N):
        ans *= mat[i][i]
    perm = [x for x in range(N)]


    solve(0, 1)
    print("#%d %.6f" % (tc, ans * 100))

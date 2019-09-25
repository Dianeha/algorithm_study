import sys
sys.stdin = open('input1861.txt', 'r')

dx = [-1, 0, 1, 0] # 위, 왼, 아래, 오
dy = [0, -1, 0, 1]

def dfs(x, y, k):
    global depth

    if not (0 <= x < N and 0 <= y < N):
        return

    if k > depth:
        depth = k

    for i in range(4):
        if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N:
            if rooms[x + dx[i]][y + dy[i]] == rooms[x][y]+1:
                dfs(x + dx[i], y + dy[i], k+1)

    return


for tc in range(1, int(input())+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    res = 1
    num = N*N

    for n in range(N):
        for m in range(N):
            depth = 1
            dfs(n, m, 1)
            if depth > res:
                res = depth
                num = rooms[n][m]
            elif depth == res:
                if num > rooms[n][m]:
                    num = rooms[n][m]

    print('#%d %d %d' %(tc, num, res))
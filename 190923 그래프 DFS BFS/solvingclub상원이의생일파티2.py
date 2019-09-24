import sys
sys.stdin = open('input5521.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    Friends = [[] for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        Friends[a].append(b)
        Friends[b].append(a)

    cnt = 0
    s = []
    start = Friends[1]
    visited[1] = 1
    if start:
        cnt += len(start)
        for x in start:
            visited[x] = 1
            s.append(x)
        while s:
            y = s.pop()
            if Friends[y]:
                for z in Friends[y]:
                    if not visited[z]:
                        visited[z] = 1
                        cnt += 1
        print("#%d %d" % (tc, cnt))
    else:
        print("#%d %d" % (tc, 0))
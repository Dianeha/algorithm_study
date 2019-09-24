import sys
sys.stdin = open('input5521.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    Friends = {}
    visited = [0 for _ in range(N+1)]
    for _ in range(M):
        a, b = input().split()
        if a in Friends.keys():
            Friends[a].append(b)
        else:
            Friends[a] = [b]

        if b in Friends.keys():
            Friends[b].append(a)
        else:
            Friends[b] = [a]

    cnt = 0
    visited[1] = 1
    s = []
    if '1' in Friends.keys():
        cnt += len(Friends['1'])
        for x in Friends['1']:
            visited[int(x)] = 1
            s.append(x)
        print(s)

        while s:
            y = s.pop() # '3'
            if y in Friends.keys():
                for z in Friends[y]:
                    if not visited[int(z)]:
                        visited[int(z)] = 1
                        cnt += 1
        print("#%d %d" % (tc, cnt))
    else:
        print("#%d %d" % (tc, 0))
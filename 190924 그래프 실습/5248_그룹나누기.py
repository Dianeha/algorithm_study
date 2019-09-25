import sys
sys.stdin = open("input5248.txt", "r")

def DFS(v):
    st.append(v)
    while st:
        v = st.pop()
        if not visited[v]:
            visited[v] = 1
            for w in edges[v]:
                if not visited[w]:
                    st.append(w)

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    vertexs = list(map(int, input().split()))
    edges = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    st = []

    while vertexs:
        x = vertexs.pop(0)
        y = vertexs.pop(0)
        edges[x].append(y)
        edges[y].append(x)

    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            cnt += 1
            DFS(i)
    print('#%d %d' % (tc, cnt))


import sys
sys.stdin = open('input7465.txt', 'r')

def DFS(s):
    st.append(s)
    while st:
        v = st.pop()
        if not visited[v]:
            visited[v] = 1
            for w in edges[v]:
                if not visited[w]:
                    st.append(w)

def BFS(v):
    q = []
    q.append(v)
    while q:
        v = q.pop(0)
        if not visited[v]:
            visited[v] = 1
            for w in edges[v]:
                if not visited[w]:
                    q.append(w)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    edges = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    visited = [0 for _ in range(N+1)]
    st = []

    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            cnt += 1
            # DFS(i)
            BFS(i)
    print('#%d %d' % (tc, cnt))

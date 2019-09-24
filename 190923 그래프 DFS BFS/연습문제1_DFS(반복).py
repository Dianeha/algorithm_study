from collections import deque

#쌤
def DFSr(v):
    print(v, end=" ")
    visited[v] = True

    for w in edges[v]:
        if not visited[w]:
            DFSr(w)

def DFS(v):
    st.append(v)
    while st:
        v = st.pop()
        if not visited[v]:
            visited[v] = 1
            print(v, end=" ")
            for w in edges[v]:
                if not visited[w]:
                    st.append(w)

tin = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
visited = [0] * (8)
edges = [[] for _ in range(8)]
st = deque()
visited = [0]*8

while tin:
    x = tin.pop(0)
    y = tin.pop(0)
    edges[x].append(y)
    edges[y].append(x)

print(edges)
DFS(1)
print()
visited = [0] * (8)
DFSr(1)
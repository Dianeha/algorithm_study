def BFS(v):
    q = []
    q.append(v)
    while q:
        v = q.pop(0)
        if not visited[v]:
            visited[v] = 1
            print(v, end=" ")
            for w in edges[v]:
                if not visited[w]:
                    q.append(w)

tin = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
visited = [0] * (8)
edges = [[] for _ in range(8)]
visited = [0]*8

while tin:
    x = tin.pop(0)
    y = tin.pop(0)
    edges[x].append(y)
    edges[y].append(x)

BFS(1)
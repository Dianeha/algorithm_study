vertexs = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
visited = [True] + [False]*7
stack = []
arr = [[0 for col in range(8)] for row in range(8)]
res = [1]

for i in range(0, len(vertexs), 2):
    arr[vertexs[i]][vertexs[i+1]] = 1
    arr[vertexs[i+1]][vertexs[i]] = 1

v = 1
visited[v] = True
while stack:
    for w in range(1, 8):
        if arr[v][w] == 1 and visited[w] == False:
            stack.append(v)
    while visited[w] == False:
        visited[w] = True
        res.append(w)
        stack.append(w)
        v = w
        for i in range(1, 8):
            if arr[v][i] == 1 and visited[i] == False:
                w = i
    v = stack.pop()

print('-'.join(map(str, res)))

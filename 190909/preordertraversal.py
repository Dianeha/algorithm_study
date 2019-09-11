input = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
linkedInfo = [[] for _ in range(14)]
nodes = list(map(int, input.split()))
nodeCnt = 0
for i in range(0, len(nodes), 2):
    linkedInfo[nodes[i]].append(nodes[i+1])

def preorder(n):
    print(n, end=' ')
    if linkedInfo[n]:
        preorder(linkedInfo[n][0])
        if len(linkedInfo[n]) == 2:
            preorder(linkedInfo[n][1])


preorder(1)
# print(linkedInfo)
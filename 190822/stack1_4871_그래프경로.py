import sys
sys.stdin = open("input_stack1_4871.txt", "r")

T = int(input())
for tc in range(1, T+1):
    VE = list(map(int, input().split()))
    V, E = VE[0], VE[1]

    # arr = [[0 for r in range(V+1)] for c in range(V+1)]
    edges = []
    for _ in range(E):
        edges.append(input().split())

    goal = input().split()

    link = goal[1]
    for edge in edges:
        if edge[0] == goal[0]:
            link = edge[1]
print(vertex)
    #
    # i = int(goal[0])
    # while True:
    #     for j range(len(arr)):
    #         arr[i][j]:
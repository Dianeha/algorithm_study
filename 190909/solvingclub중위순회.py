import sys
sys.stdin = open('중위순회.txt', 'r')

def inorder_traverse(T):
    global res
    if T:
        inorder_traverse(tree[T][1])
        # print(apb[T])
        res += tree[T][0]
        inorder_traverse(tree[T][2])

    return res

for tc in range(1, 11):
    N = int(input())
    tree = [[0] * 3 for _ in range(N + 1)]
    # apb = [0] * (N + 1)

    for i in range(N):
        templ = list(map(str, input().split()))
        tree[int(templ[0])][0] = templ[1]
        if len(templ) > 2:
            tree[int(templ[0])][1] = int(templ[2])
        if len(templ) > 3:
            tree[int(templ[0])][2] = int(templ[3])

    res = ''
    print('#%d %s' %(tc, inorder_traverse(1)))

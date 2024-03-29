# 전위/중위/후위 순회

def preorder_traverse(T):
    if T:
        print(T, end=' ')
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])


def inorder_traverse(T):
    if T:
        preorder_traverse(tree[T][0])
        print(T, end=' ')
        preorder_traverse(tree[T][1])


def postorder_traverse(T):
    if T:
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])
        print(T, end=' ')


n = 13
tree = [[0] * 2 for _ in range(n + 1)]
input = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'
templ = list(map(int, input.split()))

for i in range(len(templ) // 2):
    parent, child = templ[i * 2], templ[i * 2 + 1]
    if not tree[parent][0]:
        tree[parent][0] = child
    else:
        tree[parent][1] = child
print(tree)

preorder_traverse(1)
print()
inorder_traverse(1)
print()
postorder_traverse(1)
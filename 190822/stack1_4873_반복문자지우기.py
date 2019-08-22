import sys
sys.stdin = open("stack1_4873.txt", "r")


def find(str):
    stack = []
    top = -1

    for i, apb in enumerate(str):
        if i == 0:
            stack.append(apb)
            top += 1
        elif stack != [] and apb == stack[top]:
            stack.pop(top)
            top -= 1
        else:
            stack.append(apb)
            top += 1
    return len(stack)


T = int(input())
for tc in range(1, T+1):
    str = input()
    print('#{} {}'.format(tc, find(str)))
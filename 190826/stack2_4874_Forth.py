import sys
sys.stdin = open("input_stack2_4874.txt", "r")


def cal(i, b, f):
    if i == '+':
        return f + b
    elif i == '-':
        return f - b
    elif i == '/':
        return f//b
    elif i == '*':
        return f*b


for tc in range(1, int(input())+1):
    postfix = input().split()
    stack = []
    operaters = '+-/*'

    for i in postfix:
        if i not in operaters and i !='.':
            stack.append(int(i))
        elif i in operaters:
            if len(stack) < 2:
                res = 'error'
                break
            b = stack.pop()
            f = stack.pop()
            stack.append(cal(i, b, f))
        elif i == '.':
            if len(stack) != 1:
                res = 'error'
                break
            res = stack.pop()

    print('#{} {}'.format(tc, res))
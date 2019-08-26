import sys
sys.stdin = open("input_problem.txt", "r")


def postfix_notation(infix):
    stack_o = []
    top = -1
    postfix = []

    for i in infix:
        if i not in operaters:
            postfix.append(i)
        else:
            if i in '(*':
                stack_o.append(i)
                top += 1
            elif i == '+':
                while stack_o[top] == "*":
                    postfix.append(stack_o.pop())
                    top -= 1
                stack_o.append(i)
                top += 1
            elif i == ')':
                while stack_o[top] != '(':
                    postfix.append(stack_o.pop())
                    top -= 1
                stack_o.pop()
                top -= 1
    return postfix

def cal(postfix):
    stack = []

    for i in postfix:
        if i not in operaters:
            stack.append(int(i))
        elif i in operaters:
            b = stack.pop()
            f = stack.pop()

            if i == '+':
                stack.append(f + b)
            elif i == '*':
                stack.append(f * b)
    return stack.pop()


operaters = '+*()'
for tc in range(1, 11):
    l = input()
    infix = input()
    print('#{} {}'.format(tc, cal(postfix_notation(infix))))
    # print('#{} {}'.format(tc, postfix_notation(infix)))
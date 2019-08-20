import sys
sys.stdin = open("checkParentheses.py", "r")


def check_parentheses(input_str):
    open = ['(', '[', '{']
    close = [')', ']', '}']
    stack = []

    for i in input_str:
        if i in open:
            stack.append(i)
        elif i in close:
            if len(stack) == 0:
                return 0
            else:
                matching = stack.pop(-1)
                if open.index(matching) == close.index(i):
                    continue
                else:
                    return 0
        else:  # 괄호가 아닌 문자
            continue

    if stack:
        return 0
    else:
        return 1


T = int(input())
for tc in range(1, T+1):
    input_str = input()
    print('#{} {}'.format(tc, check_parentheses(input_str)))

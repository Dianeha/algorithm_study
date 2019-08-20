input_str = input()
open = ['(', '[', '{']
close = [')', ']', '}']
stack = []

for i in input_str:
    if i in open:
        stack.append(i)
    elif i in close:
        if len(stack) == 0:
            print('남는 close 괄호가 존재합니다.')
        else:
            matching = stack.pop(-1)
            if open.index(matching) == close.index(i):
                continue
            else:
                print('잘못된 짝이 존재합니다.')
    else:
        continue

if stack:
    print('남는 open 괄호가 존재합니다.')

infix = '2+3*4/5'
stack = []
res = []
operators = '+-*/'

for i in infix:
    if i in operators:
        stack.append(i)
    else:
        res.append(i)

for i in range(len(stack)):
    res.append(stack.pop())

print(' '.join(res))

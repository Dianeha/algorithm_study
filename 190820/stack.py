def push(list, item):
    s = list
    s.append(item)
    print(s)

def pop(list):
    if len(list) == 0:
        #underflow
        return
    else:
        return list.pop(-1)

list = []
push(list, 'a')
push(list, '12')
push(list, 534)

print(pop(list), list)
print(pop(list), list)
print(pop(list), list)
print(pop(list), pop(list) == None)
# 퀵정렬

tc1 = [11, 45, 23, 81, 28, 34]
tc2 = [11, 45, 23, 81, 28, 34, 99, 22, 17, 8]
tc3 = [1,1,1,1,1,0,0,0,0,0]

# hoare-partition 알고리즘
def partition(list, l, r):
    pivot = list[l]
    i = l
    j = r

    while i <= j:
        while list[i] <= pivot and i<r:
            i += 1
        while list[j] >= pivot and j>l:
            j -= 1
        if i < j:
            list[i], list[j] = list[j], list[i]

    list[l], list[j] = list[j], list[l]
    return j

def quickSort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quickSort(A, l, s-1)
        quickSort(A, s+1, r)

def quickSort2(l, start, end):
    if end - start <= 0:
        return

    pivot = l[end]
    i = start

    for j in range(start, end):
        if l[j] <= pivot:
            l[i], l[j] = l[j], l[i]
            i += 1
    l[i], l[end] = l[end], l[i]

    quickSort2(l, start, i-1)
    quickSort2(l, i+1, end)

quickSort2(tc1, 0, len(tc1)-1)
print(tc1)
quickSort2(tc2, 0, len(tc2)-1)
print(tc2)
quickSort2(tc3, 0, len(tc3)-1)
print(tc3)



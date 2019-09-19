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

    quickSort2(l, start, i - 1)
    quickSort2(l, i + 1, end)


for tc in range(1, int(input()) + 1):
    N = int(input())
    A = list(map(int, input().split()))
    quickSort2(A, 0, len(A) - 1)
    print('#%d %d' % (tc, A[N // 2]))
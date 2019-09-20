import sys
import time
sys.stdin = open("input5204.txt", "r")

def MergeSort(L):
    global cnt
    global N

    n = len(L)
    if n <= 2:
        if n ==2 and L[0] > L[1]:
            cnt += 1
            L.sort()
        return L
    g1 = MergeSort(L[:n//2])
    g2 = MergeSort(L[n//2:])
    if g1[-1] > g2[-1]:
        cnt += 1

    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))

    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

stime = time.time()
for tc in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    cnt = 0
    res = MergeSort(nums)
    print('#%d %d %d' %(tc, res[N//2], cnt))
print(time.time()-stime)
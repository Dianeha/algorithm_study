import sys
import time
sys.stdin = open("input5204.txt", "r")

def MergeSort(L):
    global cnt
    global N

    n = len(L)
    if n <= 2:
        if n == 2 and L[0] > L[1]:
            cnt += 1
            L[0], L[1] = L[1], L[0]
            return
        return
    g1 = L[:n//2]
    g2 = L[n//2:]
    MergeSort(g1)
    MergeSort(g2)
    if g1[-1] > g2[-1]:
        cnt += 1

    ig1, ig2, iL = 0, 0, 0
    while ig1 < len(g1) and ig2 < len(g2):
        if g1[ig1] < g2[ig2]:
            L[iL] = g1[ig1]
            ig1 += 1
            iL += 1
        else:
            L[iL] = g2[ig2]
            ig2 += 1
            iL += 1

    while ig1 < len(g1):
        L[iL] = g1[ig1]
        ig1 += 1
        iL += 1

    while ig2 < len(g2):
        L[iL] = g2[ig2]
        ig2 += 1
        iL += 1

stime = time.time()
for tc in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    cnt = 0
    MergeSort(nums)
    print('#%d %d %d' %(tc, nums[N//2], cnt))

print(time.time()-stime)

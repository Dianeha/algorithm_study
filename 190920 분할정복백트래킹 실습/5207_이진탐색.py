import sys
sys.stdin = open("input5207.txt", "r")

def BinarySearch(L, x):
    global cnt
    start = 0
    end = len(L)-1

    while start <= end:
        mid = (start+end)//2
        if x == L[mid]:
            return
        elif x > L[mid]:
            start = mid + 1
            checkLR.append('R')
        else:
            end = mid - 1
            checkLR.append('L')
    return


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    for x in B:
        if x in A:
            checkLR = []
            BinarySearch(A, x)
            f = 0
            if not checkLR or len(checkLR) == 1:
                cnt += 1
            else:
                for i in range(len(checkLR)-1):
                    if checkLR[i] == checkLR[i+1]:
                        f = 1
                        break
                if not f:
                    cnt += 1
    print('#%d %d' % (tc, cnt))





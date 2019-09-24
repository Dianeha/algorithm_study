import sys
from collections import deque
sys.stdin = open("input3074.txt", "r")

def Bsearch(start, end):

    while start < end:
        mid = (start+end)//2
        pp = 0
        for x in Times:
            pp += mid//x
        if pp < M:
            start = mid + 1
        else:
            end = mid
    return start

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    Times = [int(input()) for _ in range(N)]
    start = min(Times)
    end = M * min(Times)
    print('#%d %d' % (tc, Bsearch(start, end)))
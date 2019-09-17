import sys
sys.stdin = open('input.txt', 'r')

def perm(k, val):
    global ans
    global cnt
    cnt += 1
    if k == N:
        
        tr.append(nums)
        print(nums)
    else:
        for i in range(k, N):
            nums[k], nums[i] = nums[i], nums[k]
            perm(k + 1)
            nums[k], nums[i] = nums[i], nums[k]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    nums = [i for i in range(N)]

    cnt = 0
    ans = 0

    perm(0, 1)
    print(tr)

    # maxP = 0
    # for idx, selecs in enumerate(tr, start=1):
    #     prob = 1
    #     for selec in selecs:
    #         prob *= arr[idx][selec]/100
    #     prob *= 100
    #
    #     if prob > maxP:
    #         maxP = prob
    #
    # print(maxP)



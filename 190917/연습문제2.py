# 6자리 숫자에 대해서 완전 검색을 적용해 베이비진 검사

arr = [1,2,4,7,8,3]

def perm(n, k):
    if k == n:
        print(arr)
    else:
        for i in range(k, n-1):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k + 1)
            arr[k], arr[i] = arr[i], arr[k]

perm(6, 5)

import itertools

Nums = ['124783', '667767', '054060', '101123']
for num in Nums:
    numlist = list(num)
    mypermuatation = itertools.permutations(numlist)

    # permlist = list(mypermuatation)
    # for perm in permlist:
    #     print(perm)
    #     for i in perm:
    #         print(i)
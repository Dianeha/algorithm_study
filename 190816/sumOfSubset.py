import sys
sys.stdin = open("input2.txt", "r")

T = int(input())
setA = [x for x in range(1, 13)]
for tc in range(1, T+1):
    data = list(map(int, input().split()))

    cnt = 0
    for i in range(1, 1 << len(setA)):
        subset = []
        sum = 0
        for j in range(len(setA)):
            if i & (1 << j):
                subset.append(setA[j])
                # 별도의 리스트를 만들지 않고 sum += j+1 해도 된다.(인덱스에 1 더한게 원소값이 되므로)
                sum += setA[j]
        # info[0]: 부분집합 원소의 수 N / info[1]: 부분 집합의 합 K
        if len(subset) == data[0] and sum == data[1]:
            cnt += 1

    print('#{} {}'.format(tc, cnt))

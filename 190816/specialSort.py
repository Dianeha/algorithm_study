import sys
sys.stdin = open("input4.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    for i in range(n):
        # 나올 수 있는 정수가 1<=ai<=100 이므로
        maxIndex = minIndex = i
        if i % 2:
            for j in range(i+1, n):
                if numbers[minIndex] > numbers[j]:
                    minIndex = j
            numbers[i], numbers[minIndex] = numbers[minIndex], numbers[i]
        else:
            for j in range(i+1, n):
                if numbers[maxIndex] < numbers[j]:
                    maxIndex = j
            numbers[i], numbers[maxIndex] = numbers[maxIndex], numbers[i]

    print('#{} {}'.format(tc, ' '.join(map(str, numbers[:10]))))

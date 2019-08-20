import sys
sys.stdin = open("input5.txt", "r")

for tc in range(1, int(input())+1):
    n = int(input())
    data = list(map(int, input().split()))

    data_dict = {}
    for num in data:
        if num in data_dict:
            data_dict[num] += 1
        else:
            data_dict[num] = 1

    for k, v in data_dict.items():
        if v == 1 and (data.index(k) % 2) == 0:
            start = k

    result = []
    for i in range(len(data)//2):
        result.append(start)
        result.append(data[data.index(start)+1])
        a = data[data.index(start) + 1]
        data[data.index(start) + 1] = 0
        data[data.index(start)] = 0
        start = a

    print('#{} {}'.format(tc, ' '.join(map(str, result))))
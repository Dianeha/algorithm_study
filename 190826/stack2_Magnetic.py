import sys
sys.stdin = open('input_Magnetic.txt', 'r')

for tc in range(1, 11):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for i in range(n):
        test = []
        for j in range(n):
            if table[j][i]:
                if test == []:
                    test.append(table[j][i])
                elif table[j][i] != test[-1]:
                    test.append(table[j][i])
        test.append(0)

        while len(test) > 2:
            if test[0] == 1 and test[1] == 2:
                test.pop(0)
                test.pop(0)
                cnt += 1
            elif test[0] == 2:
                test.pop(0)

    print("#{} {}".format(tc, cnt))

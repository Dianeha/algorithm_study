import sys
sys.stdin = open("input3.txt", "r")

def binarySearch(P, Pa, Pb):
    start = 1
    end = P
    cnt_Pa = 0
    while True:
        middle = int((start + end)/2)
        cnt_Pa += 1
        if Pa < middle:
            end = middle
        elif middle < Pa:
            start = middle
        else:
            break

    start = 1
    end = P
    cnt_Pb = 0
    while True:
        middle = int((start + end)/2)
        cnt_Pb += 1
        if Pb < middle:
            end = middle
        elif middle < Pb:
            start = middle
        else:
            break

    if cnt_Pa > cnt_Pb:
        return 'B'
    elif cnt_Pa == cnt_Pb:
        return 0
    else:
        return 'A'

T = int(input())
for tc in range(1, T + 1):
    input_data = list(map(int, input().split()))
    P = input_data[0]
    Pa = input_data[1]
    Pb = input_data[2]
    print("#{} {}".format(tc, binarySearch(P, Pa, Pb)))
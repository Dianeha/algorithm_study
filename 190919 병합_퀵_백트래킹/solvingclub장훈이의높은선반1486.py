import sys
sys.stdin = open('input1486.txt')

for tc in range(1, int(input()) + 1):
    clerks, height = map(int, input().split())
    A = list(map(int, input().split()))

    # print(clerks, height, A)

import sys
sys.stdin = open("input.txt", 'r')

N = int(input())
listTime = [0 for _ in range(N+1)]
listPay = [0 for _ in range(N+1)]
TF = [0 for _ in range(N+1)]
for i in range(1, N+1):
    T, P = map(int, input().split())
    listTime[i] = T
    listPay[i] = P

k = 1
sum = 0
while k < N:

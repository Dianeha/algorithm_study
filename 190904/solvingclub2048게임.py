import sys
sys.stdin = open('input2048게임.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    p, q = map(int, input().split())

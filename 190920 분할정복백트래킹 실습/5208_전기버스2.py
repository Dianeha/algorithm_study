import sys
sys.stdin = open('input5209.txt', 'r')

def findMin(k, val):
    global ans


TC = int(input())
for tc in range(1, TC + 1):
    chargingSpot = [list(map(int, input().split()))]
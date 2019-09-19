import sys
sys.stdin = open("input5203.txt",'r')

def babyJin(list):
    player1 = [0 for i in range(10)]
    player2 = [0 for i in range(10)]

    for i in range(12):
        if not i%2:
            player1[list[i]] += 1
            if player1[list[i]] == 3:
                return 1
            if run(player1):
                return 1

        elif i%2:
            player2[list[i]] += 1
            if player2[list[i]] == 3:
                return 2
            if run(player2):
                return 2

    return 0


def run(list):
    for i in range(8):
        if list[i] >=1 and list[i+1] >=1 and list[i+2] >=1:
            return True
    return False


for tc in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    print('#%d %d' %(tc, babyJin(cards)))
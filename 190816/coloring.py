import sys
sys.stdin = open("input1.txt", "r")

def coloring(areas):
    red = []
    blue = []
    # 마지막 숫자가 1이면 red 에 넣고/ 2면 blue에 넣는다.
    for area in areas:
        if area[-1] == 1:
            for i in range(area[0], area[2] + 1):
                for j in range(area[1], area[3] + 1):
                    red.append((i, j))
        elif area[-1] == 2:
            for i in range(area[0], area[2] + 1):
                for j in range(area[1], area[3] + 1):
                    blue.append((i, j))

    # red와 blue set 안에 tuple을 비교하면서 겹치는 좌표의 갯수를 센다
    cnt = 0
    red = set(red)
    blue = set(blue)
    if len(red) >= len(blue):
        for xy in blue:
            if xy in red:
                cnt += 1
        return cnt
    else:
        for xy in red:
            if xy in blue:
                cnt += 1
        return cnt

T = int(input())
for tc in range(1, T+1):
    numOfAreas = int(input())
    areas = [list(map(int, input().split())) for _ in range(numOfAreas)]
    print('#%d %d' % (tc, coloring(areas)))

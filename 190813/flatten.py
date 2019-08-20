import sys
sys.stdin = open("input5.txt", "r")


def flatten(dump, boxes):
    for n in range(dump):
        boxes.sort()
        boxes[0] += 1
        boxes[-1] -= 1
    boxes.sort()
    return boxes[-1] - boxes[0]


T = 10
for test_case in range(1, T + 1):
    dump = int(input())
    boxes = list(map(int, input().split()))
    print('#%d %d' % (test_case, flatten(dump, boxes)))
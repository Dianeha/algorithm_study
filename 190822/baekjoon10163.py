import sys
sys.stdin = open("input.txt", "r")

res = []
for i in range(4):
    rec_points = list(map(int, input().split()))
    x1, y1 = rec_points[0], rec_points[1]
    x2, y2 = rec_points[2], rec_points[3]

    for i in range(x1, x2):
        for j in range(y1, y2):
            res.append((i, j))

print(len(set(res)))
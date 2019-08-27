import sys
sys.stdin = open("input_test.txt", "r")

for tc in range(1, int(input())+1):
    N = int(input())
    atoms = [list(map(int, input().split())) for i in range(N)]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    sec = 0
    for i in range(3): # 원자들이 영원히 충돌하지 않을 때까지
        print('{}초 후'.format(sec))
        print(atoms)
        for a in atoms:
            a[0] += dx[a[2]]
            a[1] += dy[a[2]]
        sec += 1
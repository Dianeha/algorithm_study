import sys
sys.stdin = open("모의테스트A2_input.txt", "r")

for tc in range(1, int(input())+1):
    N = int(input())
    atoms = [list(map(int, input().split())) for i in range(N)]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]


    sec = 1
    e = 0

    for i in range(3):  # 원자들이 영원히 충돌하지 않을 때까지
        atomXYDict = {}
        for idx, a in enumerate(atoms):
            a[0] += dx[a[2]]
            a[1] += dy[a[2]]

            key = str(a[0]) + str(a[1])
            if atomXYDict == {}:
                atomXYDict[key] = [idx]
            else:
                for i in atomXYDict.keys():
                    if i == key:
                        atomXYDict[i] += [idx]
                        break
                    else:
                        atomXYDict[key] = [idx]
                        break


        print('{}초 후'.format(sec))
        print(atoms)
        print(atomXYDict)
        sec += 1
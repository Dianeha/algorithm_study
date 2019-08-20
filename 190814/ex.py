arr = [
    [9, 20, 2, 18, 11],
    [19, 1, 25, 3, 21],
    [8, 24, 10, 17, 7],
    [15, 4, 16, 5, 6],
    [12, 13, 22, 23, 14],
]

a = []
for i in arr:
    a.extend(i)

min = arr[0][0]
for i in range(5):
    for j in range(i + 1, len(a)):
        if a[min] > a[j]:
            min = j
    a[i], a[min] = a[min], a[i]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

4가지 방향
벽에 부딪히면 어떻게 방향 트는지 설정

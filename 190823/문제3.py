def start(N, area):
    for i in range(N):
        for j in range(N):
            if area[i][j]:
                return i, j


def push(v):
    global top
    stack.append(v)
    top += 1


def pop(v):
    global top
    stack.pop(top)
    top -= 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]

    # 8방향 이웃한 지면 시계방향으로 탐색에 이용
    searching_x = [-1, -1, -1, 0, 1, 1, 1, 0]
    searching_y = [-1, 0, 1, 1, 1, 0, -1, -1]
    stack = []
    visited = []
    top = -1

    x, y = start(N, area)[0], start(N, area)[1]
    push((x, y))
    print(stack)

    while stack:
    # 8방향 이웃한 지면 시계방향으로 탐색
        for i in range(8):
            w = area[x + searching_x[i]][y + searching_y[i]]
            if w != 0 and (x + searching_x[i], y + searching_y[i]) not in visited:
                visited.append((x, y))
                x = x+searching_x[i]
                y = y+searching_y[i]
                push((x, y))
                break
        # pop((x, y))



# 아이디어 메모
# 1. 섬의 시작점을 배열에서 찾음
# 2. 연결된 섬들을 DFS 방식으로 탐색해나가고 방문한 단위지역은 visited에 넣으며 진행
# 3. 한 단위지역의 주변 8지역에 unvisited 된 지역 중 모두 0이 남았을 경우 > 섬이 하나 완성 > 섬 count += 1
# 4. 나머지 unvisited 영역에서 새로운 섬의 시작점을 찾음
# 5. 위 2-3번의 방법을 반복해 총 섬의 개수를 찾아나감

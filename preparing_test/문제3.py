# def start(N, area):
#     for i in range(N):
#         for j in range(N):
#             if area[i][j]:
#                 return i, j
#
#
# def push(v):
#     global top
#     stack.append(v)
#     top += 1
#
#
# def pop(v):
#     global top
#     stack.pop(top)
#     top -= 1
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     area = [list(map(int, input().split())) for _ in range(N)]
#
#     # 8방향 이웃한 지면 시계방향으로 탐색에 이용
#     searching_x = [-1, -1, -1, 0, 1, 1, 1, 0]
#     searching_y = [-1, 0, 1, 1, 1, 0, -1, -1]
#     stack = []
#     visited = []
#     top = -1
#
#     x, y = start(N, area)[0], start(N, area)[1]
#     push((x, y))
#     print(stack)
#
#     while stack:
#     # 8방향 이웃한 지면 시계방향으로 탐색
#         for i in range(8):
#             w = area[x + searching_x[i]][y + searching_y[i]]
#             if w != 0 and (x + searching_x[i], y + searching_y[i]) not in visited:
#                 visited.append((x, y))
#                 x = x+searching_x[i]
#                 y = y+searching_y[i]
#                 push((x, y))
#                 break
#         # pop((x, y))
#
#
#
# # 아이디어 메모
# # 1. 섬의 시작점을 배열에서 찾음
# # 2. 연결된 섬들을 DFS 방식으로 탐색해나가고 방문한 단위지역은 visited에 넣으며 진행
# # 3. 한 단위지역의 주변 8지역에 unvisited 된 지역 중 모두 0이 남았을 경우 > 섬이 하나 완성 > 섬 count += 1
# # 4. 나머지 unvisited 영역에서 새로운 섬의 시작점을 찾음
# # 5. 위 2-3번의 방법을 반복해 총 섬의 개수를 찾아나감

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    zero_list = [0] * N
    board = []
    result = 0
    flag = 1

    for n in range(N):
        n_list = list(map(int, input().split()))
        board.append(n_list)

    board.append(zero_list)


# 모든 matrix의 합이 0이 될때까지 반복
# i, j로 가면서 가장 먼저 걸리는 땅을 기준으로
# 밑, 우, 좌우 대각선의 순서로 계속 내려간다
# 해당 index를 저장했다가, 해당 index에 포함되는 섬을 모두 0으로 바꾼다
# 반복

    while flag == 1:
        if flag == 0:
            break
        result += 1
        a = b = 0  # start_index = (a, b)
        max_top = max_bottom = max_right = 0

        for i in range(N):
            if max_top > 0:
                break
            for j in range(N):
                if board[i][j] >= 1:
                    max_top = i
                    a = i
                    b = j
                    break

# 하, 우, 좌우밑 대각선 모두 0이 될때까지
        while board[a + 1][b] > 0 or board[a][b + 1] > 0 or board[a + 1][b - 1] > 0 or board[a + 1][b + 1] > 0:


            if board[a + 1][b] > 0:
                a += 1
                if b >= max_right:
                    max_right = b
            elif board[a][b + 1] > 0:
                b += 1
                if b >= max_right:
                    max_right = b
            elif board[a + 1][b + 1] > 0:
                a += 1
                b += 1
                if b >= max_right:
                    max_right = b
            elif board[a + 1][b - 1] > 0:
                a += 1
                b -= 1
                if b >= max_right:
                    max_right = b
            max_bottom = a
            # 섬 하나 탐색 완료

            # end_index = a, b = 11, 5
            for i in range(max_bottom + 1):
                for j in range(max_right + 1):
                    board[i][j] = 0

            # 섬이 남아있는지 확인
            count = 0
            for i in range(N):
                for j in range(N):
                    count += board[i][j]
            if count == 0:
                flag = 0
                break

    print('#{} {}'.format(t, result))
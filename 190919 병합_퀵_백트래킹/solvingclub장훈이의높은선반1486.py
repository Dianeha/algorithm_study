import sys
sys.stdin = open('input1486.txt')

### 선생님 풀이 사진에 있음
## 재평쓰 풀이 , 은영이 풀이도 확인
for tc in range(1, int(input()) + 1):
    clerks, height = map(int, input().split())
    A = list(map(int, input().split()))

    # print(clerks, height, A)


def find_top(height, result, cur):
    global min_value
    if cur == N:
        if result >= B and (result - B) < min_value:
            min_value = result - B
    else:
        find_top(height, result, cur + 1)

        result += height[cur]
        if (result - B) < min_value:
            find_top(height, result, cur + 1)
        result -= height[cur] # 회복해주기

    # else:
    #     find_top(height, result, cur + 1)
    #
    #     if (result - B) < min_value:
    #         find_top(height, result + height[cur], cur + 1)




T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    min_value = 10000

    find_top(height, 0, 0)

    print('#{} {}'.format(t, min_value))
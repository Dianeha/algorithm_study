import sys
sys.stdin = open("input4.txt", "r")


def section_sum(nm, numbers):
    n = nm[0]
    m = nm[1]

    max_sum = min_sum = sum(numbers[0:m])
    for i in range(1, n+1):
        section_sum = sum(numbers[i:i+m])
        if section_sum > max_sum:
            max_sum = section_sum
        if section_sum < min_sum:
            min_sum = section_sum

        if i == (n - m):
            return max_sum - min_sum


T = int(input())
for test_case in range(1, T + 1):
    nm = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    print('#%d %d' % (test_case, section_sum(nm, numbers)))
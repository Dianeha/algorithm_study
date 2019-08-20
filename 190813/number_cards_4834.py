import sys
sys.stdin = open("input3.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    total_cards = int(input())
    card_nums = [i for i in input()]

    result = {}
    for card_num in card_nums:
        result[card_num] = card_nums.count(card_num)

    target = max(list(result.values()))
    card = 0
    for k, v in result.items():
        if v == target and int(k) > card:
            card = int(k)

    print('#{} {} {}'.format(test_case, card, target))
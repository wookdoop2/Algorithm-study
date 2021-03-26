# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/1748

from collections import Counter

N = int(input())
answer = []

for _ in range(N):
    _list_ = list(map(int, input().split()))

    dice_dict = Counter(_list_).most_common()

    # case1
    if len(dice_dict) == 1:
        answer.append(50000 + (dice_dict[0][0] * 5000))

    if len(dice_dict) == 2:
        # case2
        if dice_dict[0][1] == 3:
            answer.append(10000 + (dice_dict[0][0] * 1000))
        # case3
        if dice_dict[0][1] == 2:
            answer.append(2000 + (dice_dict[0][0] * 500) + (dice_dict[1][0] * 500))

    # case4
    if len(dice_dict) == 3:
        answer.append(1000 + (dice_dict[0][0] * 100))

    # case5
    if len(dice_dict) == 4:
        answer.append(max(_list_) * 100)

# 답 출력
print(max(answer))

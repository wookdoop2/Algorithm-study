# Programmers
# level 3
# https://programmers.co.kr/learn/courses/30/lessons/70130
# 월간 코드 챌린지 시즌 1
from collections import Counter


def solution(a):
    answer = 0

    items = Counter(a)
    # print(items)

    for key in items.keys():

        if items[key] <= answer:
            continue

        idx = 0
        count = 0

        while idx < len(a) - 1:

            if (a[idx] != key and a[idx + 1] != key) or (a[idx] == a[idx + 1]):
                idx += 1
                continue

            count += 1
            idx += 2

        answer = max(count, answer)

    return answer * 2

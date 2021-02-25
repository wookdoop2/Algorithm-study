# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/72411
# 2021 KAKAO BLINK RECRUITMENT
from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for i in course:
        
        _list_ = []

        for order in orders:
            for c in combinations(order, i):
                _list_.append(''.join(sorted(c)))

        count_list = Counter(_list_).most_common()

        for menu, count in count_list:
            if count > 1 and count == count_list[0][1]:
                answer.append(menu)

    return sorted(answer)

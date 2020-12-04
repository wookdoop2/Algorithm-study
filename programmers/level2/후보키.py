# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/42888
# 2019 KAKAO BLINK RECRUITMENT
# Reference : https://eda-ai-lab.tistory.com/505
from itertools import combinations


def solution(relation):
    row_length = len(relation)
    col_length = len(relation[0])

    candidates = []

    for i in range(1, col_length + 1):
        candidates.extend(combinations(list(range(col_length)), i))

    # print(candidates)

    final = []
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]
        # print(tmp)
        if len(set(tmp)) == row_length:
            final.append(keys)

    print(final)

    answer = set(final)
    for i in range(len(final)):
        for j in range(i + 1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])

    return len(answer)

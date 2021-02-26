# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/72412
# 2021 KAKAO BLINK RECRUITMENT
from itertools import combinations
import bisect


def solution(info, query):
    answer = []
    info_dict = {}

    for _info_ in info:
        data = _info_.split(" ")
        career = data[:-1]
        score = int(data[-1])

        for i in range(5):
            for c in combinations(career, i):
                comb = ''.join(c)
                if comb not in info_dict.keys():
                    info_dict[comb] = [score]
                else:
                    info_dict[comb].append(score)

    for i in info_dict.values():
        i.sort()

    for i in range(len(query)):
        q = query[i].replace("and ", "")
        q = q.replace("-", "")
        data = q.split(" ")
        request_career = ''.join(data[:-1])
        request_score = int(data[-1])

        # 이진탐색
        if request_career in info_dict:
            idx = bisect.bisect_left(info_dict[request_career], request_score)
            answer.append(len(info_dict[request_career]) - idx)
        else:
            answer.append(0)

    return answer

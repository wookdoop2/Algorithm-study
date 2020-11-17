# Programmers
# level 2
# Hash
# https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1
    _dict_ = {}

    # clothes' dictionary
    # add none(no cloth) when new sort of cloth added
    for i in clothes:
        key_list = list(_dict_.keys())
        if i[1] in key_list:
            _dict_[i[1]] += 1
        else:
            _dict_[i[1]] = 2

    for i in list(_dict_.values()):
        answer *= i

    # except situation that don't wear anything
    return answer - 1

# Programmers
# level 2
# Dynamic Programming
# https://programmers.co.kr/learn/courses/30/lessons/12945
def solution(n):
    answer = 0
    max_num = 1234567

    _list_ = [0] * 100001
    _list_[1] = 1

    for i in range(2, len(_list_)):
        tmp = _list_[i - 1] + _list_[i - 2]
        _list_[i] = tmp % max_num

    answer = _list_[n]

    return answer

# Programmers
# level 3
# Dynamic Programming
# https://programmers.co.kr/learn/courses/30/lessons/12900
def solution(n):
    answer = 0
    max_num = 1000000007

    _list_ = [0] * (n + 1)

    _list_[1] = 1
    _list_[2] = 2

    for i in range(3, n + 1):
        _list_[i] = _list_[i - 1] + _list_[i - 2]
        _list_[i] %= max_num

    return _list_[n]

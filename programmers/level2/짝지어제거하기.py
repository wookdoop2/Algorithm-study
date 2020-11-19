# Programmers
# level 2
# Stack
# https://programmers.co.kr/learn/courses/30/lessons/12973
# 2017 팁스타운
def solution(s):
    _list_ = []

    s = list(s)
    for i in s:
        if len(_list_) == 0:
            _list_.append(i)
        elif _list_[-1] == i:
            _list_.pop()
        else:
            _list_.append(i)

    if len(_list_) == 0:
        return 1
    else:
        return 0

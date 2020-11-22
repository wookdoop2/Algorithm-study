# Programmers
# level 2
# Dynamic Programming
# https://programmers.co.kr/learn/courses/30/lessons/12913
def solution(land):
    answer = 0

    _list_ = [[0] * 4 for _ in range(len(land))]

    _list_[0][0] = land[0][0]
    _list_[0][1] = land[0][1]
    _list_[0][2] = land[0][2]
    _list_[0][3] = land[0][3]

    for i in range(1, len(land)):
        _list_[i][0] = max(_list_[i - 1][1] + land[i][0],
                           _list_[i - 1][2] + land[i][0], _list_[i - 1][3] + land[i][0])
        _list_[i][1] = max(_list_[i - 1][0] + land[i][1],
                           _list_[i - 1][2] + land[i][1], _list_[i - 1][3] + land[i][1])
        _list_[i][2] = max(_list_[i - 1][0] + land[i][2],
                           _list_[i - 1][1] + land[i][2], _list_[i - 1][3] + land[i][2])
        _list_[i][3] = max(_list_[i - 1][0] + land[i][3],
                           _list_[i - 1][1] + land[i][3], _list_[i - 1][2] + land[i][3])
    answer = max(_list_[len(land) - 1])
    return answer

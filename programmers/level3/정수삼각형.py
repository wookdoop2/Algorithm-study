# Programmers
# level 3
# https://programmers.co.kr/learn/courses/30/lessons/43105
# 동적계획법(Dynamic Programming)
def solution(triangle):

    _list_ = [[0] * i for i in range(1, len(triangle) + 1)]

    _list_[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0:
                _list_[i][j] = _list_[i - 1][j] + triangle[i][j]
            elif j == i:
                _list_[i][j] = _list_[i - 1][j - 1] + triangle[i][j]
            else:
                _list_[i][j] = max(_list_[i - 1][j - 1] + triangle[i][j], _list_[i - 1][j] + triangle[i][j])

    return max(_list_[-1])

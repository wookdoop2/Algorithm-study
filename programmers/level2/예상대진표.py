# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/12985
# 2017 팁스타운
def solution(n, a, b):
    answer = 1
    count = 0
    players = list(range(1, n + 1))

    while n != 1:
        n = n // 2
        count += 1

    _list_ = [[0] * (2 ** i) for i in range(count, 0, -1)]

    _list_[0] = players

    # 아래부터 대진표 짜기
    for i in range(1, len(_list_)):
        for j in range(len(_list_[i - 1]) // 2):
            tmp = [0, 0]
            tmp[0] = _list_[i - 1][2 * j]
            tmp[1] = _list_[i - 1][(2 * j) + 1]

            if a in tmp and b in tmp:
                return answer
            elif a in tmp:
                _list_[i][j] = a
            elif b in tmp:
                _list_[i][j] = b
            else:
                _list_[i][j] = tmp[0]

        # print(_list_)

        answer += 1
    return answer

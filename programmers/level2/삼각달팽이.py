# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/68645
def solution(n):
    answer = []

    _list_ = [[0] * n for _ in range(n)]
    y = -1
    x = 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            _list_[y][x] = num
            num += 1

    for i in range(n):
        for j in range(0, i + 1):
            answer.append(_list_[i][j])

    return answer

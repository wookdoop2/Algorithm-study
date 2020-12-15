# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/12899
def decimal_to_124(num):

    notation = "124"

    q, r = divmod(num - 1, 3)
    n = notation[r]

    if q == 0:
        return n
    else:
        return decimal_to_124(q) + n


def solution(n):

    answer = decimal_to_124(n)

    return answer

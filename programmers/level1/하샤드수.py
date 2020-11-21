# Programmers
# level 1
# https://programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    answer = True
    _sum_ = 0

    new_list = list(str(x))

    for i in new_list:
        _sum_ = _sum_ + int(i)
    if x % _sum_ == 0:
        return answer
    else:
        answer = False
        return answer

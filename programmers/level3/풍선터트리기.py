# Programmers
# level 3
# https://programmers.co.kr/learn/courses/30/lessons/12900
# 월간 코드 챌린지 시즌 1
def solution(a):
    answer = 0
    # 양 옆의 숫자들이 기준 숫자보다 작을 떄 ->
    # 번호가 더 작은 풍선을 2번 터트려야함 ->
    # 무조건 마지막까지 남을 수 없음
    _list_ = []
    for i in range(len(a)):
        if i == 0:
            # right_min = min(a[1:])
            _list_.append(a[i])
        elif i == len(a) - 1:
            # left_min = min(a[:i])
            _list_.append(a[i])
        else:
            left_min = min(a[:i])
            right_min = min(a[i + 1:])

            if a[i] > left_min and a[i] > right_min:
                continue
            else:
                _list_.append(a[i])
    answer = len(_list_)
    return answer

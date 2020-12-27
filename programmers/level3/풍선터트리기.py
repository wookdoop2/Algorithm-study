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
    min_left = [0] * len(a)
    min_right = [0] * len(a)

    min_num = a[0]
    for i in range(1, len(a)):
        min_left[i] = min_num

        if a[i] < min_num:
            min_num = a[i]

    min_num = a[-1]
    for i in range(len(a) - 2, 0, -1):
        min_right[i] = min_num

        if a[i] < min_num:
            min_num = a[i]

    # print(min_left)
    # print(min_right)

    for i in range(len(a)):
        if i == 0 or i == len(a) - 1:
            _list_.append(a[i])
        else:
            if a[i] > min_left[i] and a[i] > min_right[i]:
                continue
            else:
                _list_.append(a[i])

    # print(_list_)
    answer = len(_list_)

    return answer

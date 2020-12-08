# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/17687
# 2018 KAKAO BLINK RECRUITMENT

# decimal number to base n number
def decimal_to_base(num, base):
    notation = "0123456789ABCDEF"

    q, r = divmod(num, base)
    n = notation[r]

    return decimal_to_base(q, base) + n if q else n


def solution(n, t, m, p):
    answer = ''
    _list_ = []

    # List of numbers as many as the number of games
    start_num = 0
    while True:
        check = 0
        tmp = decimal_to_base(start_num, n)
        for i in range(len(tmp)):
            _list_.append(tmp[i])
            if len(_list_) == t * m:
                check = 1
                break

        if check == 1:
            break
        else:
            start_num += 1
            continue

    # print(_list_)
    # print(len(_list_))

    for i in range(len(_list_)):
        if p - 1 == i % m:
            answer += str(_list_[i])

    return answer

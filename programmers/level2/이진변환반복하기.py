# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/70129
# 월간 코드 챌린지 시즌1
def decimal_to_binary(num):
    binary_num = []
    while True:
        if num % 2 == 0:
            binary_num.insert(0, '0')
        else:
            binary_num.insert(0, '1')

        num = num // 2

        if num == 1:
            binary_num.insert(0, '1')
            break
        elif num == 0:
            binary_num.insert(0, '0')
            break

    return binary_num


def solution(s):
    answer = []
    count = 0
    count_zero = 0

    while True:
        _list_ = []
        s = list(map(int, s))
        for i in s:
            if i == 1:
                _list_.append(i)
            else:
                count_zero += 1
        s = decimal_to_binary(len(_list_))

        if int(''.join(s)) == '10':
            break
        count += 1
    return count, count_zero

# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/70129
# 월간 코드 챌린지 시즌1
def decimal_to_binary(num):
    if num == 1:
        return '1'
    return decimal_to_binary(num // 2) + str(num % 2)


def solution(s):
    count = 0
    count_zero = 0

    while s != '1':
        count_one = 0
        s = list(s)
        for i in s:
            if i == '1':
                count_one += 1
            else:
                count_zero += 1
        s = decimal_to_binary(count_one)

        count += 1

    return count, count_zero

# Programmers
# level 2
# GCD & LCM
# https://programmers.co.kr/learn/courses/30/lessons/12953
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def solution(arr):
    answer = arr[0]

    for i in range(1, len(arr)):
        answer = (answer * arr[i]) / gcd(answer, arr[i])

    return answer

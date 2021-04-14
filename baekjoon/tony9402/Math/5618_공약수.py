# Baekjoon Online Judge
# Data Structure
# https://www.acmicpc.net/problem/5618
# 출처 : https://github.com/tony9402/baekjoon

import sys


def gcd(a, b):

    while b != 0:
        a, b = b, a % b

    return a


input = sys.stdin.readline

n = int(input())
_list_ = sorted(list(map(int, input().split())))
answer = []

if len(_list_) == 2:
    gcd_num = gcd(_list_[1], _list_[0])

    # 1 2 3 6
    # 1 2 3 4 6 12
    # 1 3 9 27
    for i in range(1, int(gcd_num ** 0.5) + 1):
        if gcd_num % i == 0:
            answer.append(i)
            answer.append(int(gcd_num / i))

else:
    gcd_num = gcd(_list_[2], gcd(_list_[1], _list_[0]))

    for i in range(1, int(gcd_num ** 0.5) + 1):
        if gcd_num % i == 0:
            answer.append(i)
            answer.append(int(gcd_num / i))

for num in sorted(set(answer)):
    print(num)

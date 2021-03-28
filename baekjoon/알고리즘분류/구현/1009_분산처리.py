# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/1009

import sys

input = sys.stdin.readline

T = int(input())

# 어떤 수를 제곱했을때 1의 자리 숫자는 4개의 숫자 묶음 규칙이 번갈아가며 계속 반복된다라고 가정
_list_ = [[0] * 4 for _ in range(10)]

for i in range(10):
    _list_[i][0] = i
    for j in range(1, 4):
        _list_[i][j] = (_list_[i][j - 1] * i) % 10

for _ in range(T):
    a, b = map(int, input().split())

    if a % 10 == 0:
        print(10)
    else:
        print(_list_[a % 10][(b % 4) - 1])

# 시간 초과
# for _ in range(T):
#     a, b = map(int, input().split())
#
#     if a == 0:
#         print(0)
#         continue
#     elif a == 1:
#         print(1)
#         continue
#     elif a == 5:
#         print(5)
#         continue
#     elif a == 6:
#         print(6)
#         continue
#
#     _list_ = []
#     num = 1
#
#     for _ in range(b):
#         num *= a
#         _list_.append(num % 10)
#
#     print(_list_[len(_list_) % 10 - 1])

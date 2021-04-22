# Baekjoon Online Judge
# Prefix Sum
# https://www.acmicpc.net/problem/14929
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

if n == 1:
    print(num_list[0])
    exit()

if n == 2:
    print(num_list[0] * num_list[1])
    exit()

_list_ = [0] * n
_list_[0] = num_list[0]
_list_[1] = num_list[0] * num_list[1]

for i in range(2, n):
    _list_[i] = num_list[i] * (_list_[i - 1] + _list_[i - 2]) + _list_[i - 1]

print(_list_[n - 1])

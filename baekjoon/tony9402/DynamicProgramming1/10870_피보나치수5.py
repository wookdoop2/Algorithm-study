# Baekjoon Online Judge
# Data Structure
# https://www.acmicpc.net/problem/10870
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

n = int(input())

_list_ = [0] * 21
_list_[0] = 0
_list_[1] = 1

for i in range(2, 21):
    _list_[i] = _list_[i - 1] + _list_[i - 2]

print(_list_[n])
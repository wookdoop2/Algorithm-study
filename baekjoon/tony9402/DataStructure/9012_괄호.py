# Baekjoon Online Judge
# Data Structure
# https://www.acmicpc.net/problem/9012
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    strings = list(input().rstrip())

    _list_ = []

    for string in strings:

        # list가 비어있으면 무조건 넣어주기기
        if len(_list_) == 0:
            _list_.append(string)
            continue

        # '(' 다음에 바로 ')'가 올 때 '(' pop해주기
        if _list_[-1] == '(' and string == ')':
            _list_.pop()
            continue

        _list_.append(string)

    if len(_list_) == 0:
        print("YES")
    else:
        print("NO")

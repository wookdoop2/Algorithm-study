# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/1475
N = list(map(int, input()))

_list_ = []
for i in range(10):
    _list_.append(N.count(i))

if _list_[6] > 0 or _list_[9] > 0:
    if (_list_[6] + _list_[9]) % 2 > 0:
        _list_[9] = (_list_[6] + _list_[9]) // 2 + 1
    else:
        _list_[9] = (_list_[6] + _list_[9]) // 2
    _list_[6] = 0

print(max(_list_))

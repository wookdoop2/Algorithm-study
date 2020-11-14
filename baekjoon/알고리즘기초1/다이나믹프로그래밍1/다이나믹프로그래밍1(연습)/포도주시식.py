# Baekjoon Online Judge
# Dynamic Programming
# https://www.acmicpc.net/problem/2156
n = int(input())

_list_ = [[0] * 3 for _ in range(n)]

_list_[0][1] = int(input())

for i in range(1, n):
    cost = int(input())

    _list_[i][0] = max(_list_[i - 1][0], _list_[i - 1][1], _list_[i - 1][2])
    _list_[i][1] = _list_[i - 1][0] + cost
    _list_[i][2] = _list_[i - 1][1] + cost

print(max(_list_[n - 1]))

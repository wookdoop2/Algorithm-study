# Baekjoon Online Judge
# Dynamic Programming
# https://www.acmicpc.net/problem/11722
n = int(input())

cost = list(map(int, input().split()))

_list_ = [0] * n
_list_[0] = 1

for i in range(1, n):
    _list_[i] = 1
    for j in range(i):
        if cost[j] > cost[i] and _list_[i] < _list_[j] + 1:
            _list_[i] = _list_[j] + 1

print(max(_list_))

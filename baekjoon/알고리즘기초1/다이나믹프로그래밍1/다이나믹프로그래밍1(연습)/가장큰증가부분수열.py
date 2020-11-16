# Baekjoon Online Judge
# Dynamic Programming
# https://www.acmicpc.net/problem/11055
n = int(input())

cost = list(map(int, input().split()))

_list_ = [0] * n

_list_[0] = cost[0]

for i in range(1, n):
    _list_[i] = cost[i]
    for j in range(i):
        if cost[j] < cost[i] and _list_[i] < _list_[j] + cost[i]:
            _list_[i] = _list_[j] + cost[i]

print(max(_list_))

# 2 1 5 6 7
# 2 1 1 2 5

# Baekjoon Online Judge
# Dynamic Programming
# https://www.acmicpc.net/problem/1932
n = int(input())

_list_ = []

for i in range(1, n + 1):
    _list_.append([0] * n)

for i in range(n):
    cost = list(map(int, input().split()))
    if i == 0:
        _list_[i][0] = cost[0]
        continue

    for j in range(i + 1):
        if j == 0:
            _list_[i][j] = _list_[i - 1][j] + cost[j]
        elif j == i:
            _list_[i][j] = _list_[i - 1][j - 1] + cost[j]
        else:
            _list_[i][j] = max(_list_[i - 1][j - 1] + cost[j], _list_[i - 1][j] + cost[j])

print(max(_list_[-1]))

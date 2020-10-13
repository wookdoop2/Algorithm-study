# Bottom-Up
N = int(input())
cost = list(map(int, input().split()))

_list_ = [10000] * (N + 1)
_list_[0] = 0

for i in range(1, N + 1):
    for j in range(1, i + 1):
        _list_[i] = min(_list_[i], cost[j - 1] + _list_[i - j])
print(_list_[N])

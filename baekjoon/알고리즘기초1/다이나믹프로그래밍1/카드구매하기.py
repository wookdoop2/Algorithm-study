# Bottom-Up
N = int(input())
cost = list(map(int, input().split()))

_list_ = [0] * (N + 1)
_list_[1] = 1

for i in range(2, N + 1):
    for j in range(1, i + 1):
        _list_[i] = max(_list_[i], cost[j - 1] + _list_[i - j])
print(_list_[N])

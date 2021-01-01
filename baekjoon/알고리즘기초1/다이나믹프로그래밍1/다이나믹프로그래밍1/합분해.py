# Baekjoon Online Judge
# Dynamic Programming
num, count = map(int, input().split())

mod_num = 1000000000

_list_ = [[0] * (count + 1) for _ in range(num + 1)]

for i in range(0, num + 1):
    for j in range(1, count + 1):
        if j == 1:
            _list_[i][j] = 1
            continue
        for k in range(0, i + 1):
            _list_[i][j] += _list_[i - k][j - 1]
        _list_[i][j] %= mod_num

print(_list_[num][count])

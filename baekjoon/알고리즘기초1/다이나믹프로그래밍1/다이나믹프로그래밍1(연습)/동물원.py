# Baekjoon Online Judge
# Dynamic Programming
n = int(input())

mod_num = 9901
_list_ = [[0] * 3 for _ in range(n)]

_list_[0][0] = 1
_list_[0][1] = 1
_list_[0][2] = 1

for i in range(1, n):
    _list_[i][0] = _list_[i - 1][0] + _list_[i - 1][1] + _list_[i - 1][2]
    _list_[i][0] %= mod_num
    _list_[i][1] = _list_[i - 1][0] + _list_[i - 1][2]
    _list_[i][1] %= mod_num
    _list_[i][2] = _list_[i - 1][0] + _list_[i - 1][1]
    _list_[i][2] %= mod_num

print(sum(_list_[n - 1]) % mod_num)

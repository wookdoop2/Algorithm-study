# Baekjoon Online Judge
# Dynamic Programming
mod_num = 1000000009
max_num = 1000000

_list_ = [0] * (max_num + 1)
_list_[1] = 1
_list_[2] = 2
_list_[3] = 4

for i in range(4, max_num + 1):
    _list_[i] = _list_[i - 1] + _list_[i - 2] + _list_[i - 3]
    _list_[i] %= mod_num

count = int(input())

for i in range(count):
    num = int(input())
    print(_list_[num])

# Baekjoon Online Judge
# Dynamic Programming
max_num = 100000
_list_ = [0] * (max_num + 1)

_list_[1] = 1

num = 1

for i in range(1, max_num + 1):
    if i == num ** 2:
        num += 1
        _list_[i] = 1
        index = i
        continue
    else:
        _list_[i] = min(_list_[i - 1] + 1, 1 + _list_[i - num ** 2])

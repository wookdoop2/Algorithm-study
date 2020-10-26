# Baekjoon Online Judge
# Dynamic Programming
max_num = int(input())
_list_ = [0] * (max_num + 1)

for i in range(1, max_num + 1):
    num = 1
    _list_[i] = i
    while num * num <= i:
        if _list_[i] > _list_[i - (num * num)] + 1:
            _list_[i] = _list_[i - (num * num)] + 1
        num += 1

print(_list_[max_num])

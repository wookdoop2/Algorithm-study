# Beakjoon Online Judge
# Dynamic Programming
max_num = 90
_list_ = [[0] * 2 for _ in range(max_num + 1)]

_list_[1][1] = 1
_list_[2][0] = 1

for i in range(3, max_num + 1):
    for j in range(0, 2):
        if j == 0:
            _list_[i][j] = _list_[i - 1][j] + _list_[i - 1][j - 1]
        else:
            _list_[i][j] = _list_[i - 1][j - 1]

num = int(input())
print(sum(_list_[num]))

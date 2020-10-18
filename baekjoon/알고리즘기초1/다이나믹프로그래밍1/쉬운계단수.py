# Beakjoon Online Judge
# Dynamic Programming
mod_num = 1000000000
_list_ = [[0] * 10 for _ in range(100 + 1)]
for i in range(1, len(_list_[1])):
    _list_[1][i] = 1

for i in range(2, len(_list_)):
    for j in range(10):
        if j == 0:
            _list_[i][j] = _list_[i - 1][j + 1]
        elif j == 9:
            _list_[i][j] = _list_[i - 1][j - 1]
        else:
            _list_[i][j] = _list_[i - 1][j - 1] + _list_[i - 1][j + 1]

        _list_[i][j] %= mod_num

num = int(input())
print(sum(_list_[num]) % mod_num)

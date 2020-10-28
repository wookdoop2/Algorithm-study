# Baekjoon Online Judge
# Dynamic Programming
n = int(input())

mod_num = 10007
_list_ = [[0] * 10 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(0, 10):
        if i == 1:
            _list_[i][j] = 1
        for k in range(0, j + 1):
            _list_[i][j] += _list_[i - 1][j - k]
            _list_[i][j] %= mod_num

print(sum(_list_[n]) % mod_num)

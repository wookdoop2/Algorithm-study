# Baekjoon Online Judge
# Dynamic Programming
max_num = 100000
mod_num = 1000000009
_list_ = [[0] * 4 for _ in range(max_num + 1)]

_list_[1][1] = 1
_list_[2][2] = 1
_list_[3][1] = 1
_list_[3][2] = 1
_list_[3][3] = 1

for i in range(4, max_num + 1):
    _list_[i][1] = _list_[i - 1][2] + _list_[i - 1][3]
    _list_[i][2] = _list_[i - 2][1] + _list_[i - 2][3]
    _list_[i][3] = _list_[i - 3][1] + _list_[i - 3][2]

    # 메모리 초과를 없애기 위해 1000000009로 나눈 나머지를 할당
    _list_[i][1] %= mod_num
    _list_[i][2] %= mod_num
    _list_[i][3] %= mod_num

count = int(input())
for i in range(count):
    num = int(input())
    print(sum(_list_[num]) % mod_num)

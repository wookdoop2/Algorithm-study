count = int(input())

_list_ = [0] * 11
_list_[1] = 1
_list_[2] = 2
_list_[3] = 4
for i in range(4, 11):
    _list_[i] = _list_[i - 1] + _list_[i - 2] + _list_[i - 3]

for i in range(count):
    num = int(input())
    print(_list_[num])

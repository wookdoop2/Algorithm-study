num, count = map(int, input().split())

_list_ = [[0] * (count + 1) for _ in range(num + 1)]

for i in range(1, num + 1):

    # logic
    for j in range(1, count + 1):
        _list_[i][j] = _list_[i][j - 1] + 1

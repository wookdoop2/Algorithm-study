T = int(input())

for test_case in range(1, T + 1):
    p, q = map(int, input().split())

    answer = 0
    _list_ = [[1, 1]]

    for i in range(2, 300):
        for j in range(1, i + 1):
            _list_.append([j, i - (j - 1)])

    _p_ = _list_[p - 1]
    _q_ = _list_[q - 1]

    new_point = [_p_[0] + _q_[0], _p_[1] + _q_[1]]

    for idx in range(len(_list_)):
        if _list_[idx] == new_point:
            answer = idx + 1
            break

    print("#{} {}".format(test_case, answer))

# 시간초과

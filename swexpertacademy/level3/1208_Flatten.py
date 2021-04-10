# SW Expert Academy
# Difficulty 3

for test_case in range(1, 11):
    dump = int(input())
    _list_ = list(map(int, input().split()))

    while dump != 0:
        max_line_idx = _list_.index(max(_list_))
        min_line_idx = _list_.index(min(_list_))

        _list_[max_line_idx] -= 1
        _list_[min_line_idx] += 1

        dump -= 1

    print("#{} {}".format(test_case, max(_list_) - min(_list_)))
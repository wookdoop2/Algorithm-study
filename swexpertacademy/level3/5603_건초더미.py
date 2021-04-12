# SW Expert Academy
# Difficulty 3

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    _list_ = []
    for _ in range(N):
        _list_.append(int(input()))

    avg = sum(_list_) // N
    count = 0
    check_count = 0

    while check_count != N - 1:

        max_idx = _list_.index(max(_list_))
        min_idx = _list_.index(min(_list_))

        while _list_[min_idx] != avg and _list_[max_idx] != avg:
            _list_[max_idx] -= 1
            _list_[min_idx] += 1
            count += 1

        check_count += 1

    print("#{} {}".format(test_case, count))

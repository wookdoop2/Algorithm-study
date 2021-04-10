# SW Expert Academy
# Difficulty 3

for test_case in range(1, 11):
    length = int(input())
    _list_ = list(map(int, input().split()))

    answer = 0

    for i in range(2, length - 2):
        b1, b2, b3, b4 = _list_[i - 2], _list_[i - 1], _list_[i + 1], _list_[i + 2]
        if _list_[i] <= max(b1, b2, b3, b4):
            continue
        else:
            answer += _list_[i] - max(b1, b2, b3, b4)

    print("#{} {}".format(test_case, answer))

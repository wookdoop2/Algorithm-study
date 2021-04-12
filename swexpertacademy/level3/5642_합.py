# SW Expert Academy
# Difficulty 3

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    _list_ = list(map(int, input().split()))

    # 시간 초과
    # for length in range(1, N + 1):
    #     for i in range(N - length + 1):
    #         answer = max(answer, sum(_list_[i:i + length]))

    answer = _list_[0]

    for i in range(N - 1):

        if _list_[i] >= 0 and _list_[i] + _list_[i + 1] >= 0:
            _list_[i + 1] = _list_[i] + _list_[i + 1]

        answer = max(answer, _list_[i + 1])

    print("#{} {}".format(test_case, answer))

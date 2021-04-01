# SW Expert Academy
# Difficulty 3

T = int(input())

for test_case in range(T):
    N = int(input())

    _list_ = []
    for _ in range(N):
        _list_.append(list(map(int, input())))

    answer = 0

    center = N // 2

    # 가운데 기준
    answer += sum(_list_[center])

    # 위쪽
    # _list_[0][3:4(7 - 3)]
    # _list_[1][2:5]
    # _list_[2][1:6]
    for i in range(center):
        answer += sum(_list_[i][center - i:N - (center - i)])

    # 아래 쪽
    # _list_[6][3(3 - (6 - 6)):4(7 - 3)]
    # _list_[5][2(3 - (6 - 5)):5(7 - 2)]
    for i in range(N - 1, center, -1):
        answer += sum(_list_[i][center - (N - 1 - i): N - (center - (N - 1 - i))])

    print("#{} {}".format(test_case + 1, answer))

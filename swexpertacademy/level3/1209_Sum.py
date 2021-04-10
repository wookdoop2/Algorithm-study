# SW Expert Academy
# Difficulty 3


def rotate_key(key, length):
    _list_ = [[] for _ in range(length)]

    for i in range(length):
        for j in range(length):
            _list_[j].insert(0, key[i][j])

    return _list_


for test_case in range(1, 11):
    N = int(input())
    length = 100
    board0 = [list(map(int, input().split())) for _ in range(length)]
    board1 = rotate_key(board0, length)

    answer = 0

    # 대각선
    tmp = 0
    for i in range(length):
        tmp += board0[i][i]
    answer = max(answer, tmp)

    # 가로, 세로
    for i in range(length):
        answer = max(answer, sum(board0[i]))
        answer = max(answer, sum(board1[i]))

    print("#{} {}".format(test_case, answer))


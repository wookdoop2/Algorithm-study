# SW Expert Academy
# Difficulty 3


def dfs(board):

    global count

    if len(board) == N:
        count += 1
        return

    _list_ = list(range(N))

    for i in range(len(board)):

        if board[i] in _list_:  # 같은 열
            _list_.remove(board[i])

        # 0(line0) -> 1
        # 1(line0) -> 2
        # 2(line0) -> 3
        # 0(line01) -> 2 (1 + 1)
        # 1(line01) -> 3 (2 + 1)
        # 2(line01) -> 4 (3 + 1)
        if board[i] + (len(board) - i) in _list_:  # 오른쪽 대각선
            _list_.remove(board[i] + (len(board) - i))

        if board[i] - (len(board) - i) in _list_:   # 왼쪽 대각선
            _list_.remove(board[i] - (len(board) - i))

    if len(_list_) != 0:
        for i in range(len(_list_)):
            board.append(_list_[i])
            dfs(board)
            board.remove(_list_[i])
    else:
        return


T = int(input())

for test_case in range(1, T + 1):

    N = int(input())

    if N == 1:
        print("#{} {}".format(test_case, 1))

    elif N == 2:
        print("#{} {}".format(test_case, 0))

    else:
        count = 0

        for start in range(N):
            dfs([start])

        print("#{} {}".format(test_case, count))

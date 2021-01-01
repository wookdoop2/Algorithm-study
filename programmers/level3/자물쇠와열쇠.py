# Programmers
# level 3
# https://programmers.co.kr/learn/courses/30/lessons/60059
# 2020 KAKAO BLIND RECRUITMENT
def rotate_key(key, length):
    _list_ = [[] * 1 for _ in range(length)]

    for i in range(length):
        for j in range(length):
            _list_[j].insert(0, key[i][j])

    return _list_


def check(M, N, board):
    count = 0
    for i in range(N):
        for j in range(N):
            if board[M + i][M + j] == 1:
                count += 1

    if count != N * N:
        return 0
    else:
        return 1


def add(start_x, start_y, N, board, key):
    for i in range(N):
        for j in range(N):
            board[start_x + i][start_y + j] += key[i][j]

    return board


def minus(start_x, start_y, N, board, key):
    for i in range(N):
        for j in range(N):
            board[start_x + i][start_y + j] -= key[i][j]

    return board


def solution(key, lock):
    answer = True
    M = len(key)
    N = len(lock)

    board = [[0] * (2 * M + N) for _ in range(2 * M + N)]
    for i in range(N):
        for j in range(N):
            board[M + i][M + j] = lock[i][j]

    # print(board)

    for i in range(4):
        key = rotate_key(key, M)
        for m in range(len(board) - N):
            for n in range(len(board) - N):
                board = add(m, n, N, board, key)
                if check(M, N, board) == 1:
                    return True
                else:
                    board = minus(m, n, N, board, key)

    return False

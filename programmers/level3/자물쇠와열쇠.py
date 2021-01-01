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
        return False
    else:
        return True


def add(y, x, M, board, key):
    for i in range(M):
        for j in range(M):
            board[y + i][x + j] += key[i][j]

    return board


def minus(y, x, M, board, key):
    for i in range(M):
        for j in range(M):
            board[y + i][x + j] -= key[i][j]

    return board


def solution(key, lock):
    M = len(key)
    N = len(lock)

    board = [[0] * (2 * M + N) for _ in range(2 * M + N)]
    for i in range(N):
        for j in range(N):
            board[M + i][M + j] = lock[i][j]

    # print(board)

    for i in range(4):
        key = rotate_key(key, M)
        for start_y in range(len(board) - (M - 1)):
            for start_x in range(len(board) - (M - 1)):
                board = add(start_y, start_x, M, board, key)
                if check(M, N, board) == True:
                    return True
                else:
                    board = minus(start_y, start_x, M, board, key)

    return False

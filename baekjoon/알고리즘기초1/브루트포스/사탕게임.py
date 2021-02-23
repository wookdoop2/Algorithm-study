# Baekjoon Online Judge
# 알고리즘 기초 1 - Brute Force
# https://www.acmicpc.net/problem/3085
N = int(input())
_list_ = [list(input()) for _ in range(N)]
answer = 0


def check_max_num(board):

    final_max_num = 0

    for i in range(N):

        horizontal_count = 1
        vertical_count = 1

        for j in range(1, N):
            if board[i][j - 1] == board[i][j]:
                horizontal_count += 1
            else:
                horizontal_count = 1

            final_max_num = max(final_max_num, horizontal_count)

        for j in range(1, N):
            if board[j - 1][i] == board[j][i]:
                vertical_count += 1
            else:
                vertical_count = 1

            final_max_num = max(final_max_num, vertical_count)

    return final_max_num


for i in range(N):
    for j in range(N):

        if j + 1 < N:
            if _list_[i][j] != _list_[i][j + 1]:
                tmp = _list_[i][j]
                _list_[i][j] = _list_[i][j + 1]
                _list_[i][j + 1] = tmp

                answer = max(answer, check_max_num(_list_))

                tmp = _list_[i][j]
                _list_[i][j] = _list_[i][j + 1]
                _list_[i][j + 1] = tmp

        if i + 1 < N:
            if _list_[i][j] != _list_[i + 1][j]:
                tmp = _list_[i][j]
                _list_[i][j] = _list_[i + 1][j]
                _list_[i + 1][j] = tmp

                answer = max(answer, check_max_num(_list_))

                tmp = _list_[i][j]
                _list_[i][j] = _list_[i + 1][j]
                _list_[i + 1][j] = tmp
print(answer)

# Baekjoon Online Judge
# Dynamic Programming 2
# https://www.acmicpc.net/problem/15724
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline
MAX = 1025

N, M = map(int, input().split())
board = [[0] * MAX for _ in range(MAX)]
answer_board = [[0] * MAX for _ in range(MAX)]

for i in range(1, N + 1):
    _list_ = list(map(int, input().split()))
    for j in range(len(_list_)):
        board[i][j + 1] = _list_[j]

for i in range(1, MAX):
    for j in range(1, MAX):
        if i == 1 and j == 1:
            answer_board[i][j] = board[i][j]
            continue

        if i == 1:
            answer_board[i][j] = answer_board[i][j - 1] + board[i][j]
            continue

        if j == 1:
            answer_board[i][j] = answer_board[i - 1][j] + board[i][j]
            continue

        answer_board[i][j] = answer_board[i - 1][j] + answer_board[i][j - 1] - answer_board[i - 1][j - 1] + board[i][j]

for i in range(N + 1):
    print(answer_board[i])

K = int(input())

for _ in range(K):

    x1, y1, x2, y2 = map(int, input().split())

    print(answer_board[x2][y2] - (answer_board[x1 - 1][y2] + answer_board[x2][y1 - 1] - answer_board[x1 - 1][y1 - 1]))

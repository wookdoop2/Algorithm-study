# Baekjoon Online Judge
# Divide & Conquer
# https://www.acmicpc.net/problem/17829
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline


def pulling(board, n):

    if n == 1:
        return board[0][0]

    tmp = [[] for _ in range(n // 2)]
    for i in range(0, n, 2):
        for j in range(0, n, 2):

            tmp_list = sorted([board[i][j], board[i + 1][j], board[i][j + 1], board[i + 1][j + 1]])
            tmp[i // 2].append(tmp_list[2])

    return pulling(tmp, n // 2)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

print(pulling(board, N))

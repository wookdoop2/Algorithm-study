# Baekjoon Online Judge
# Prefix Sum
# https://www.acmicpc.net/problem/2167
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

sum_board = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            sum_board[i][j] = board[0][0]
        elif i == 0:
            sum_board[i][j] += board[i][j] + sum_board[i][j - 1]
        elif j == 0:
            sum_board[i][j] += board[i][j] + sum_board[i - 1][j]
        else:
            sum_board[i][j] += sum_board[i - 1][j]
            for k in range(j + 1):
                sum_board[i][j] += board[i][k]

K = int(input())

for _ in range(K):

    i, j, x, y = map(int, input().split())
    start_y, start_x, end_y, end_x = i - 1, j - 1, x - 1, y - 1

    # 시간 초과
    # answer = 0
    #
    # if start_y == end_y:
    #     for j in range(start_x, end_x + 1):
    #         answer += board[start_y][j]
    # elif start_x == end_x:
    #     for i in range(start_y, end_y + 1):
    #         answer += board[i][start_x]
    # elif start_y == end_y and start_x == end_y:
    #     answer = board[start_y][start_x]
    # else:
    #     for i in range(start_y, end_y + 1):
    #         answer += sum(board[i][start_x:end_x + 1])
    #
    # print(answer)

    if i == 1 and j == 1:
        print(sum_board[x - 1][y - 1])
    elif i == 1:
        print(sum_board[x - 1][y - 1] - sum_board[x - 1][j - 2])
    elif j == 1:
        print(sum_board[x - 1][y - 1] - sum_board[i - 2][y - 1])
    else:
        print(sum_board[x - 1][y - 1] - sum_board[i - 2][y - 1] - sum_board[x - 1][j - 2] + sum_board[i - 2][j - 2])


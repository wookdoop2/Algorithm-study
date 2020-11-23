# Programmers
# level 2
# Dynamic Programming
# https://programmers.co.kr/learn/courses/30/lessons/12905
def solution(board):
    width = len(board[0])
    height = len(board)

    for i in range(1, height):
        for j in range(1, width):
            if board[i][j] > 0:
                board[i][j] = min(board[i - 1][j - 1], board[i][j - 1], board[i - 1][j]) + 1

    max_num = 0

    for i in range(height):
        for j in range(width):
            if max_num < board[i][j]:
                max_num = board[i][j]

    return max_num ** 2

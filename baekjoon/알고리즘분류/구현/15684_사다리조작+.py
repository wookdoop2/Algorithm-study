# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/15684

import sys


# i번 세로선의 결과가 i번이 나오면
def check():
    for n in range(1, N + 1):
        current = n
        for h in range(1, H + 1):
            if board[h][current] == 1:
                current += 1
            elif board[h][current - 1] == 1:
                current -= 1

        if current != n:
            return False

    return True


def dfs(start, count):
    global answer

    if count >= answer:
        return

    if check():
        answer = count
        return

    for i in range(start, len(empty_list)):
        y, x = empty_list[i]
        if x == 1:
            if board[y][x + 1] != 1:
                board[y][x] = 1
                dfs(i + 1, count + 1)
                board[y][x] = 0
        elif x == N - 1:
            if board[y][x - 1] != 1:
                board[y][x] = 1
                dfs(i + 1, count + 1)
                board[y][x] = 0
        else:
            if board[y][x - 1] != 1 and board[y][x + 1] != 1:
                board[y][x] = 1
                dfs(i + 1, count + 1)
                board[y][x] = 0


input = sys.stdin.readline
N, M, H = map(int, input().split())

board = [[0] * (N + 1) for _ in range(H + 1)]
empty_list = []

for _ in range(M):
    a, b = map(int, input().split())
    board[a][b] = 1

for i in range(1, H + 1):
    for j in range(1, N):
        if board[i][j] != 1 and board[i][j - 1] != 1 and board[i][j + 1] != 1:
            empty_list.append([i, j])

# print(empty_list)

answer = 4

dfs(0, 0)

# if answer >= 4:
#     print(-1)
# else:
#     print(answer)

print(-1 if answer >= 4 else answer)

# 시간초과

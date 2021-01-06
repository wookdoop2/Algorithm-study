# Baekjoon Online Judge
# Brute Force
# https://www.acmicpc.net/problem/1018
N, M = map(int, input().split())
_list_ = []
for i in range(N):
    _list_.append(list(input()))

board = []
for i in range(M - 8 + 1):
    for j in range(N - 8 + 1):
        for y in range(j + 8):
            board.append(_list_[y][i:i+8])


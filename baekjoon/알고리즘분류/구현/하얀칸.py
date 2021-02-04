# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/1100
chess_list = []
for i in range(8):
    chess_list.append(list(input()))

count = 0
for i in range(8):
    if i % 2 == 0:
        for j in range(8):
            if j % 2 == 0 and chess_list[i][j] == 'F':
                count += 1
    else:
        for j in range(8):
            if j % 2 == 1 and chess_list[i][j] == 'F':
                count += 1

print(count)
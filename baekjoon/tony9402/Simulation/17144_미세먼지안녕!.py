# Baekjoon Online Judge
# Simulation
# https://www.acmicpc.net/problem/17144
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

di = [[-1, 0], [0, 1], [1, 0], [0, -1]]

R, C, T = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(map(int, input().split())))

for _ in range(T):

    # 미세먼지 확산
    tmp_board = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if board[y][x] >= 5:
                spread = board[y][x] // 5
                for d in di:
                    new_y, new_x = y + d[0], x + d[1]
                    if 0 <= new_y < R and 0 <= new_x < C and board[new_y][new_x] != -1:
                        tmp_board[new_y][new_x] += spread
                        board[y][x] -= spread

    # 확산된 미세먼지와 원래 미세먼지 합치기
    for i in range(R):
        for j in range(C):
            board[i][j] += tmp_board[i][j]

    for i in range(R):
        print(board[i])

    # 공기청정기 위치
    air_condition = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == -1:
                air_condition.append(i)

    ac_top, ac_bottom = air_condition

    # 공기청정기 위쪽 (시계 반대방향)
    tmp_list = []

    # 아래
    tmp_list.append(board[ac_top][-1])
    for j in range(C - 1, 0, -1):
        board[ac_top][j] = board[ac_top][j - 1]
    board[ac_top][1] = 0

    # 오른쪽
    for i in range(0, ac_top - 1):
        if i == 0:
            tmp_list.append(board[i][-1])
        board[i][-1] = board[i + 1][-1]
    board[ac_top - 1][-1] = tmp_list[0]

    # 위쪽
    tmp_list.append(board[0][0])
    for j in range(0, C - 1):
        board[0][j] = board[0][j + 1]
    board[0][C - 2] = tmp_list[1]

    # 왼쪽
    for i in range(ac_top - 1, 0, -1):
        board[i][0] = board[i - 1][0]
    board[1][0] = tmp_list[2]

    # print()
    # for i in range(R):
    #     print(board[i])

    # 공기청정기 아래쪽 (시계방향)
    tmp_list = []

    # 위쪽
    tmp_list.append(board[ac_bottom][-1])
    for j in range(C - 1, 0, -1):
        board[ac_bottom][j] = board[ac_bottom][j - 1]
    board[ac_bottom][1] = 0

    # 오른쪽
    tmp_list.append(board[-1][-1])
    for i in range(R - 1, ac_bottom, -1):
        board[i][-1] = board[i - 1][-1]
    board[ac_bottom + 1][-1] = tmp_list[0]

    # 아래쪽
    tmp_list.append(board[-1][0])
    for j in range(0, C - 1):
        board[-1][j] = board[-1][j + 1]
    board[-1][C - 2] = tmp_list[1]

    # 왼쪽
    for i in range(ac_bottom + 1, R - 2):
        board[i][0] = board[i + 1][0]
    board[R - 2][0] = tmp_list[2]

    # print()
    # for i in range(R):
    #     print(board[i])

# 미세먼지 양 측정
answer = 0
for i in range(R):
    for j in range(C):
        answer += board[i][j]

print(answer + 2)
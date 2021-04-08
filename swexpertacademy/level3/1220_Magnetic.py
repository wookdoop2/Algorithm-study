# SW Expert Academy
# Difficulty 3

# dy = [0, 1, -1]
# dx = [0, 0, 0]
#
#
# def change(x):
#
#     global board
#     flag = 0
#
#     while flag != 2:
#         for y in range(N):
#             b = board[y][x]
#             if b == 1:
#                 if y + dy[b] >= N - 1:  # 밖으로 나가는 경우
#                     board[y][x] = 0
#                     continue
#                 if board[y + dy[b]][x + dx[b]] == 2:    # 2와 인접한 경우 스탑
#                     flag = 1
#                     continue
#                 if board[y + dy[b]][x + dx[b]] == 1 and flag == 1:
#                     flag = 2
#                     return
#
#                 board[y + dy[b]][x + dx[b]] = board[y][x]
#                 board[y][x] = 0
#
#             elif b == 2:
#                 if y + dy[b] <= 0:  # 밖으로 나가는 경우
#                     board[y][x] = 0
#                 if board[y + dy[b]][x + dx[b]] == 1:    # 1과 인접한 경우 스탑
#                     flag = 1
#                     continue
#                 if board[y + dy[b]][x + dx[b]] == 2 and flag == 1:
#                     flag = 2
#                     return
#                 board[y + dy[b]][x + dx[b]] = board[y][x]
#                 board[y][x] = 0
#
#
# for test_case in range(1, 11):
#     N = int(input())
#     board = []
#     for _ in range(N):
#         board.append(list(map(int, input().split())))
#
#     for i in range(N):
#         change(i)
#
#     answer = 0
#
#     for i in range(N - 1):
#         for j in range(N):
#             if board[i][j] == 1 and board[i + 1][j] == 2:
#                 answer += 1
#
#     print("#{} {}".format(test_case, answer))

for test_case in range(1, 11):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for i in range(N):
        state = 0
        for j in range(N):
            if board[j][i] == 1 and state == 0:
                state = 1
            elif board[j][i] == 2 and state == 1:
                state = 0
                count += 1

    print("#{} {}".format(test_case, count))

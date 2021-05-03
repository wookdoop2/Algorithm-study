# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/21608
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

# 상 우 하 좌
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

N = int(input())
class_board = [[0] * N for _ in range(N)]
prefer_list = [[] for _ in range(N ** 2 + 1)]
student_list = []

for _ in range(N ** 2):
    tmp_list = list(map(int, input().split()))
    prefer_list[tmp_list[0]] = (tmp_list[1:])
    student_list.append(tmp_list[0])

# # 처음 학생 앉히기
# idx = 0
# if N % 2 == 0:
#     class_board[1][1] = student_list[idx]
# else:
#     class_board[N // 2][N // 2] = student_list[idx]

# 다음 학생부터 시작
for idx in range(1, N ** 2):

    student = student_list[idx]
    final_y = 0
    final_x = 0
    max_prefer = -99
    max_empty = -99

    for y in range(N):
        for x in range(N):
            if class_board[y][x] == 0:

                prefer_count = 0
                empty_count = 0

                for d in dir:
                    new_y, new_x = y + d[0], x + d[1]
                    if 0 <= new_y < N and 0 <= new_x < N:
                        if class_board[new_y][new_x] in prefer_list[student]:
                            prefer_count += 1
                        elif class_board[new_y][new_x] == 0:
                            empty_count += 1

                # 좋아하는 학생이 있는 인접한 칸 | 비어있는 칸을 count하면서 최댓값이 되는 자리의 index를 저장
                if max_prefer < prefer_count or (max_prefer == prefer_count and max_empty < empty_count):
                    final_y, final_x = y, x
                    max_prefer = prefer_count
                    max_empty = empty_count

    # 자리 지정
    class_board[final_y][final_x] = student

# print(class_board)

answer = 0

for y in range(N):
    for x in range(N):

        count = 0
        student = class_board[y][x]

        for d in dir:
            new_y, new_x = y + d[0], x + d[1]
            if 0 <= new_y < N and 0 <= new_x < N:
                if class_board[new_y][new_x] in prefer_list[student]:
                    count += 1

        if count == 0:
            answer += 0
        elif count == 1:
            answer += 1
        elif count == 2:
            answer += 10
        elif count == 3:
            answer += 100
        else:
            answer += 1000

print(answer)

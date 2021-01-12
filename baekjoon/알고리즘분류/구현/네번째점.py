# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/3009
x_point_list = []
y_point_list = []
for i in range(3):
    x, y = map(int, input().split())
    x_point_list.append(x)
    y_point_list.append(y)

answer_x = 0
answer_y = 0
for i in range(3):
    if x_point_list.count(x_point_list[i]) == 1:
        answer_x = x_point_list[i]

    if y_point_list.count(y_point_list[i]) == 1:
        answer_y = y_point_list[i]

print(answer_x, answer_y)

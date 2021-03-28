# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/3190

import sys
from collections import deque


def direction_change(d_idx, c):
    if c == 'L':
        return (d_idx - 1) % 4
    else:
        return (d_idx + 1) % 4


# 시계 방향 (좌, 상, 우, 하)
d = [[0, -1], [-1, 0], [0, 1], [1, 0]]

input = sys.stdin.readline

N = int(input())

board = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 2

L = int(input())
direction_info = dict()
for _ in range(L):
    X, C = input().split()
    direction_info[int(X)] = C

time = 1
direction = 2   # 우 방향 시작
y, x = 0, 0
check_list = deque([[0, 0]])    # 갔던 장소 저장 -> index 0번째의 값 == 꼬리 위치
board[0][0] = 1

while True:

    y, x = y + d[direction][0], x + d[direction][1]

    if 0 <= y < N and 0 <= x < N and board[y][x] != 1:

        if board[y][x] != 2:    # 사과가 없을 때
            _y_, _x_ = check_list.popleft()
            board[_y_][_x_] = 0

        board[y][x] = 1
        check_list.append([y, x])

        # 방향 바꿀 시간일 때 (방향 변환 정보는 X초가 끝난 뒤에 적용됨)
        if time in direction_info.keys():
            direction = direction_change(direction, direction_info[time])

        time += 1

    else:   # 벽에 부딪히거나, 자기 몸에 맞을 경우
        break

print(time)

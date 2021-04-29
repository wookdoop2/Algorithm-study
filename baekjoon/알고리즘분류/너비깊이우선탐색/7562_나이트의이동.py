# Baekjoon Online Judge
# BFS
# https://www.acmicpc.net/problem/7562

import sys
from collections import deque

input = sys.stdin.readline

# 나이트가 이동 할 수 있는 좌표
di = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]


def bfs(_y_, _x_, d_y, d_x):

    dq = deque([[_y_, _x_]])

    while dq:

        y, x = dq.popleft()

        # 이동하려는 칸에 도착할 시 종료
        if y == d_y and x == d_x:
            print(visited[y][x])
            return

        for d in di:

            new_y, new_x = y + d[0], x + d[1]

            if 0 <= new_y < I and 0 <= new_x < I and visited[new_y][new_x] == 0:
                dq.append([new_y, new_x])
                visited[new_y][new_x] = visited[y][x] + 1


T = int(input())

for test_case in range(T):

    I = int(input())
    visited = [[0] * I for _ in range(I)]

    start_y, start_x = map(int, input().split())
    dst_y, dst_x = map(int, input().split())

    # print(I, start_y, start_x, dst_y, dst_x)
    bfs(start_y, start_x, dst_y, dst_x)

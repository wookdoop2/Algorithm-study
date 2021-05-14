# Baekjoon Online Judge
# Shortest Path
# https://www.acmicpc.net/problem/11403
# 출처 : https://github.com/tony9402/baekjoon

import sys
from collections import deque

input = sys.stdin.readline


def bfs(start_node):

    dq = deque([start_node])
    can_go_list = []
    visited = [0] * N

    while dq:

        node = dq.popleft()

        for adjacent in range(len(board[node])):
            if board[node][adjacent] == 1 and visited[adjacent] != 1:
                dq.append(adjacent)
                visited[adjacent] = 1
                can_go_list.append(adjacent)

    # print(can_go_list)

    for idx in can_go_list:
        answer_board[start_node][idx] = 1


N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
answer_board = [[0] * N for _ in range(N)]

for i in range(N):
    bfs(i)

for i in range(N):
    print(' '.join(map(str, answer_board[i])))

# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/1844
# 찾아라 프로그래밍 마에스터
from collections import deque


def solution(maps):

    n = len(maps)
    m = len(maps[0])
    MAX = 100001

    cost_board = [[MAX] * m for _ in range(n)]

    # 상 우 하 좌
    di = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    # BFS
    dq = deque([[0, 0, 1]])  # 좌표와 지나간 칸의 개수를 deque에 넣는다
    cost_board[0][0] = 1

    while dq:

        y, x, cost = dq.popleft()

        for d in di:
            new_y, new_x = y + d[0], x + d[1]

            # 가려고 하는 위치가 맵 안에 있고, 벽이 아닐 때
            if 0 <= new_y < n and 0 <= new_x < m and maps[new_y][new_x] != 0:
                if cost_board[new_y][new_x] > cost + 1:
                    cost_board[new_y][new_x] = cost + 1
                    dq.append([new_y, new_x, cost + 1])

    # print(cost_board)
    # print(cost_board[-1][-1])

    if cost_board[-1][-1] == MAX:
        return -1
    else:
        return cost_board[-1][-1]


solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])
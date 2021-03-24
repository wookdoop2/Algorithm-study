# Programmers
# level 3
# Graph
# https://programmers.co.kr/learn/courses/30/lessons/49189
import heapq
import math


# 다익스트라 알고리즘
def dijkstra(start, board, n):
    INF = math.inf

    _list_ = [INF] * (n + 1)
    queue = []
    _list_[start] = 0
    heapq.heappush(queue, [0, start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        for adjacent in board[current_node]:
            d = current_distance + 1

            if d < _list_[adjacent]:
                _list_[adjacent] = d
                heapq.heappush(queue, [d, adjacent])

    return _list_[1:]


def solution(n, edge):
    board = [[] for _ in range(n + 1)]
    for i in range(len(edge)):
        sp, ep = edge[i]
        board[sp].append(ep)
        board[ep].append(sp)

    go_list = dijkstra(1, board, n)

    # go_list.count(max(go_list))

    return go_list.count(max(go_list))


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])

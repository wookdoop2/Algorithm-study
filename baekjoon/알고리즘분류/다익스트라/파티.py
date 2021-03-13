# Baekjoon Online Judge
# Dijkstra algorithm
# https://www.acmicpc.net/problem/1238
import heapq
import sys


def dijkstra(start, end):
    go_list = [INF] * (N + 1)
    queue = []
    go_list[start] = 0
    heapq.heappush(queue, [0, start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        for adjacent, w in enumerate(board[current_node]):
            d = current_distance + w

            if d < go_list[adjacent]:
                go_list[adjacent] = d
                heapq.heappush(queue, [d, adjacent])

    return go_list[end]


INF = 1e9
input = sys.stdin.readline

N, M, X = map(int, input().split())
board = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    start, end, weight = map(int, input().split())
    board[start][end] = weight

answer = -1

for start in range(1, N + 1):

    if start == X:
        continue

    answer = max(answer, dijkstra(start, X) + dijkstra(X, start))

print(answer)

# 시간초과

# Baekjoon Online Judge
# Dijkstra algorithm
# https://www.acmicpc.net/problem/1504
import heapq
import sys


def dijkstra(start, end):
    queue = []
    distances = [INF] * N

    distances[start - 1] = 0
    heapq.heappush(queue, [0, start - 1])

    while queue:

        current_distance, current_node = heapq.heappop(queue)

        for adjacent, weight in board[current_node]:
            d = current_distance + weight
            if d < distances[adjacent]:
                distances[adjacent] = d
                heapq.heappush(queue, [d, adjacent])

    return distances[end - 1]


input = sys.stdin.readline
INF = 1e4
N, E = map(int, input().split())
board = [[] * N for _ in range(N)]
for _ in range(E):
    x, y, d = map(int, input().split())
    board[x - 1].append([y - 1, d])
    board[y - 1].append([x - 1, d])
v1, v2 = map(int, input().split())

answer0, answer1, check0, check1 = INF, INF, 0, 0
d0 = dijkstra(1, v1)
d1 = dijkstra(v1, v2)
d2 = dijkstra(v2, v1)
d3 = dijkstra(v1, N)
d4 = dijkstra(v2, N)
d5 = dijkstra(1, v2)
# 1번 정점 -> v1 -> v2 -> N번 정점
if d0 != INF and d1 != INF and d4 != INF:
    answer0 = d0 + d1 + d4
else:
    check0 = 1
# 1번 정점 -> v2 -> v1 -> N번 정점
if d5 != INF and d2 != INF and d3 != INF:
    answer1 = d5 + d2 + d3
else:
    check1 = 1

# 경로 있는지 없는지 확인
if check0 == 1 or check1 == 1:
    print(-1)
else:
    print(min(answer0, answer1))

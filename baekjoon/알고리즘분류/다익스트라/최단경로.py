# Baekjoon Online Judge
# Dijkstra algorithm
# https://www.acmicpc.net/problem/1753
import heapq
import math

V, E = map(int, input().split())
start = int(input()) - 1

matrix = [[math.inf] * V for _ in range(V)]
for i in range(E):
    u, v, w = map(int, input().split())
    u, v = u - 1, v - 1
    matrix[u][v] = w

queue = []
distances = [math.inf] * V
distances[start] = 0
heapq.heappush(queue, [start, 0])

while queue:
    current_node, current_distance = heapq.heappop(queue)

    for adjacent, weight in enumerate(matrix[current_node]):
        d = weight + current_distance

        if distances[current_node] < current_distance:
            continue

        if d < distances[adjacent]:
            distances[adjacent] = d
            heapq.heappush(queue, [adjacent, d])

for i in distances:
    if i == math.inf:
        print("INF")
    else:
        print(i)

# 메모리 초과

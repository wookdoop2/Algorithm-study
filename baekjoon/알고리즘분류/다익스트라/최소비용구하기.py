# Baekjoon Online Judge
# Dijkstra algorithm
# https://www.acmicpc.net/problem/1916
import heapq
import sys

input = sys.stdin.readline
INF = 1e9

N = int(input())
M = int(input())

matrix = [[] for _ in range(N + 1)]
for i in range(M):
    u, v, w = map(int, input().split())
    matrix[u].append([v, w])

# print(matrix)

start, end = map(int, input().split())

queue = []
distances = [INF] * (N + 1)
distances[start] = 0
heapq.heappush(queue, [start, 0])

while queue:
    current_node, current_distance = heapq.heappop(queue)

    if current_distance > distances[current_node]:
        continue

    for adjacent, weight in matrix[current_node]:
        d = weight + current_distance

        if d < distances[adjacent]:
            distances[adjacent] = d
            heapq.heappush(queue, [adjacent, d])

print(distances[end])

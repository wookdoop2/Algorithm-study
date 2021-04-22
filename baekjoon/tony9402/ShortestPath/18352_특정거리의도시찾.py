# Baekjoon Online Judge
# Shortest Path
# https://www.acmicpc.net/problem/18352
# 출처 : https://github.com/tony9402/baekjoon

import sys
import heapq

input = sys.stdin.readline


# 다익스트라 알고리즘
def dijkstra(start):

    global answer

    INF = 1e9

    queue = []
    distance = [INF] * (N + 1)

    distance[start] = 0
    heapq.heappush(queue, [0, start])

    while queue:

        current_distance, current_node = heapq.heappop(queue)

        for adjacent in board[current_node]:

            d = current_distance + 1

            if distance[adjacent] > d:
                distance[adjacent] = d
                heapq.heappush(queue, [d, adjacent])

    # print(distance)

    for i in range(N + 1):
        if distance[i] == K:
            answer.append(i)


N, M, K, X = map(int, input().split())

board = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    board[a].append(b)

answer = []

dijkstra(X)

# 최단거리 K인 도시가 하나도 없으면 -1 출력
if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for num in answer:
        print(num)

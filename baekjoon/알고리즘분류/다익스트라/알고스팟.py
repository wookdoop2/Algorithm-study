# Baekjoon Online Judge
# Dijkstra algorithm
# https://www.acmicpc.net/problem/1261
import heapq

M, N = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(map(int, input())))

_list_ = [[-1] * M for _ in range(N)]
d = [[-1, 0], [0, -1], [1, 0], [0, 1]]

queue = []
_list_[0][0] = 0
heapq.heappush(queue, [0, [0, 0]])

while queue:
    current_distance, current_node = heapq.heappop(queue)

    for i in range(4):
        dx = d[i][0] + current_node[0]
        dy = d[i][1] + current_node[1]
        if 0 <= dx < N and 0 <= dy < M and _list_[dx][dy] == -1:
            _list_[dx][dy] = current_distance

            if maze[dx][dy] == 1:
                heapq.heappush(queue, [current_distance + 1, [dx, dy]])
            else:
                heapq.heappush(queue, [current_distance, [dx, dy]])

print(_list_[N - 1][M - 1])

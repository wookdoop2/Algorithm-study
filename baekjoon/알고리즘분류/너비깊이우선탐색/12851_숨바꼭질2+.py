# Baekjoon Online Judge
# BFS
# https://www.acmicpc.net/problem/12851

from collections import deque

MAX = 100001
N, K = map(int, input().split())

visited = [[MAX, 0] for _ in range(MAX)]
visited[N][0], visited[N][1] = 0, 1  # 0 : 최소 횟수, 1 : 루트 갯수

_list_ = deque()

_list_.append(N)

while _list_:

    node = _list_.popleft()

    for nx in [node + 1, node - 1, node * 2]:
        if 0 <= nx < MAX:
            if visited[nx][0] == MAX:
                _list_.append(nx)
                visited[nx][0] = visited[node][0] + 1
                visited[nx][1] = visited[node][1]

            elif visited[nx][0] == visited[node][0] + 1:
                visited[nx][1] += visited[node][1]

print(visited[K][0])
print(visited[K][1])

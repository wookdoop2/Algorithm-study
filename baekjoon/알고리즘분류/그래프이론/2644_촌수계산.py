# Baekjoon Online Judge
# Graph
# https://www.acmicpc.net/problem/2644
from collections import deque


def bfs(start, end):

    visited = [0] * (n + 1)
    dq = deque([[start, 0]])

    while dq:

        node, weight = dq.popleft()

        visited[node] = 1

        if node == end:
            return weight

        for adjacent in generation_list[node]:
            if visited[adjacent] != 1:
                dq.append([adjacent, weight + 1])

    return -1


n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

generation_list = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    generation_list[y].append(x)
    generation_list[x].append(y)

# print(generation_list)

# print(bfs(p1, p2))

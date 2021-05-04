# Baekjoon Online Judge
# Graph Traversal
# https://www.acmicpc.net/problem/1260
# 출처 : https://github.com/tony9402/baekjoon

import sys
from collections import deque

input = sys.stdin.readline


def dfs(start_node):

    visited[start_node] = 1
    print(start_node, end=' ')

    for adjacent in board[start_node]:
        if visited[adjacent] != 1:
            dfs(adjacent)


def bfs(start_node):

    dq = deque([start_node])

    while dq:

        node = dq.popleft()
        visited[node] = 1
        print(node, end=' ')

        for adjacent in board[node]:
            if visited[adjacent] != 1:
                dq.append(adjacent)


N, M, V = map(int, input().rstrip().split())

board = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().rstrip().split())
    board[start].append(end)
    board[end].append(start)

for i in range(1, N + 1):
    board[i].sort()

print(board)

visited = [0] * (N + 1)
dfs(V)
print()
visited = [0] * (N + 1)
bfs(V)

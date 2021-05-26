# Baekjoon Online Judge
# Tree
# https://www.acmicpc.net/problem/11725
# 출처 : https://github.com/tony9402/baekjoon

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
tree_board = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    start, end = map(int, input().split())
    tree_board[start].append(end)
    tree_board[end].append(start)

dq = deque([1])
parent_list = [0] * (N + 1)
visited = [0] * (N + 1)
visited[1] = 1

while dq:

    node = dq.popleft()

    for child in tree_board[node]:
        if visited[child] != 1:
            visited[child] = 1
            parent_list[child] = node
            dq.append(child)

for i in range(2, len(parent_list)):
    print(parent_list[i])

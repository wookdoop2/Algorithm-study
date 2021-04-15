# Baekjoon Online Judge
# Graph Traversal
# https://www.acmicpc.net/problem/2606
# 출처 : https://github.com/tony9402/baekjoon

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

computer_board = [[] for _ in range(N + 1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    computer_board[a].append(b)
    computer_board[b].append(a)

start_node = 1
visited = [0] * (N + 1)
dq = deque([1])
answer = 0

while dq:

    node = dq.popleft()

    visited[node] = 1

    for adjacent in computer_board[node]:
        if visited[adjacent] != 1:
            dq.append(adjacent)
            visited[adjacent] = 1
            answer += 1

print(answer)

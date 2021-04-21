# Baekjoon Online Judge
# DFS
# https://www.acmicpc.net/problem/11724

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(start_node):

    visited[start_node] = 1

    for adjacent in board[start_node]:
        if visited[adjacent] != 1:
            dfs(adjacent)

    return


N, M = map(int, input().split())

board = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    board[u].append(v)
    board[v].append(u)

answer = 0

for i in range(1, N + 1):
    if visited[i] != 1:
        answer += 1
        dfs(i)

print(answer)

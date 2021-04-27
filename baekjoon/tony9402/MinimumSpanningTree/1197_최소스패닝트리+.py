# Baekjoon Online Judge
# Minimum Spanning Tree
# https://www.acmicpc.net/problem/1197
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def dfs(start_node):

    global tmp_answer

    visited[start_node] = 1

    for adjacent, weight in board[start_node]:
        if visited[adjacent] != 1:
            tmp_answer += weight
            dfs(adjacent)

    return


V, E = map(int, input().split())

board = [[] for _ in range(V + 1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    board[A].append([B, C])

answer = 1e9

for start in range(1, V + 1):
    tmp_answer = 0
    visited = [0] * (V + 1)
    dfs(start)

    if 0 in visited[1:]:
        continue
    else:
        answer = min(answer, tmp_answer)

print(answer)


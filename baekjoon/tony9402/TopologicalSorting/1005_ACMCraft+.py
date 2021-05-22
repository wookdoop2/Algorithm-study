# Baekjoon Online Judge
# Topological Sorting
# https://www.acmicpc.net/problem/1005
# 출처 : https://github.com/tony9402/baekjoon

import sys
from collections import deque

input = sys.stdin.readline


def topologicalSort():

    while dq:

        target = dq.popleft()

        for adjacent in adjList[target]:
            sequence[adjacent] = max(sequence[adjacent], sequence[target] + D[adjacent])
            indegree[adjacent] -= 1

            if not indegree[adjacent]:
                dq.append(adjacent)


T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))

    sequence = [0] * (N + 1)
    indegree = [0] * (N + 1)
    adjList = [[] for _ in range(N + 1)]

    for _ in range(K):
        X, Y = map(int, input().split())

        indegree[Y] += 1
        adjList[X].append(Y)

    W = int(input())

    dq = deque()
    for i in range(1, N + 1):
        if not indegree[i]:
            sequence[i] = D[i]
            dq.append(i)

    topologicalSort()

    print(sequence[W])

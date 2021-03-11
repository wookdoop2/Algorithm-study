# Baekjoon Online Judge
# BFS DFS
# https://www.acmicpc.net/problem/1260
from collections import deque


def bfs(start):
    queue = deque()
    queue.append(start)
    check[start] = 1

    while queue:
        node = queue.popleft()

        for i in range(1, N + 1):
            if check[i] != 1 and _list_[node][i] == 1:
                queue.append(i)
                check[i] = 1

        print(node, end=' ')


def dfs(start):
    check[start] = 1

    print(start, end=' ')

    for i in range(1, N + 1):
        if check[i] != 1 and _list_[start][i] == 1:
            dfs(i)


N, M, V = map(int, input().split())
_list_ = [[0] * (N + 1) for _ in range(N + 1)]
check = [0] * (N + 1)
for i in range(M):
    node0, node1 = map(int, input().split())
    _list_[node0][node1] = 1
    _list_[node1][node0] = 1

dfs(V)
check = [0] * (N + 1)   # 초기화
print()
bfs(V)

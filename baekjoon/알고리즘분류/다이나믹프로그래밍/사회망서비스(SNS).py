# Baekjoon Online Judge
# Dynamic Programming
# https://www.acmicpc.net/problem/2533
import sys

sys.setrecursionlimit(10**9)


def dfs(cur):
    visited[cur] = 1
    for node in tree[cur]:
        if visited[node] != 1:
            child[cur].append(node)
            dfs(node)


def get_dp(current_node, check):
    if check == 1:  # 얼리어답터일 때
        # _list_[node][0] = min( get_dp(node의 자식, 0), get_dp(node의 자식, 1) )의 총 합

        if _list_[current_node][0] != -1:
            return _list_[current_node][0]

        _list_[current_node][0] = 1
        for child_node in child[current_node]:
            _list_[current_node][0] += min(get_dp(child_node, 0), get_dp(child_node, 1))
        return _list_[current_node][0]

    else:   # 얼리어답터가 아닐 때
        # _list_[node][1] = dp(node의 자식, 1)의 총 합

        if _list_[current_node][1] != -1:
            return _list_[current_node][1]

        _list_[current_node][1] = 0
        for child_node in child[current_node]:
            _list_[current_node][1] += get_dp(child_node, 1)
        return _list_[current_node][1]


input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
child = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

_list_ = [[-1, -1] for _ in range(N + 1)]   # [node가 얼리어댑터일 때, node가 얼리어댑터가 아닐 떄]
visited = [0] * (N + 1)

dfs(1)

# print(child)
# print(visited)

print(min(get_dp(1, 0), get_dp(1, 1)))

# 메모리 초과

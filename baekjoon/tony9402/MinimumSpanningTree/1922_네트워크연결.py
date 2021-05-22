# Baekjoon Online Judge
# Minimum Spanning Tree
# https://www.acmicpc.net/problem/1922
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline


def find_parent(target):

    # 부모가 자기 자신일 때
    if target == _list_[target]:
        return target

    # 재귀
    parent = find_parent(_list_[target])

    _list_[target] = parent

    return _list_[target]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        _list_[b] = a
    else:
        _list_[a] = b


N = int(input())
M = int(input())

board = [list(map(int, input().split())) for _ in range(M)]
_list_ = [i for i in range(N + 1)]

# 비용 순으로 정렬
board.sort(key=lambda x: x[2])

answer = 0

for start_node, end_node, cost in board:
    if find_parent(start_node) == find_parent(end_node):
        continue
    else:
        answer += cost
        union(start_node, end_node)

print(answer)

# Baekjoon Online Judge
# Dynamic Programming On Trees
# https://www.acmicpc.net/problem/15681
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

N, R, Q = map(int, input().split())

_tree_ = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    U, V = map(int, input().split())
    _tree_[U].append(V)

for _ in range(Q):
    U = int(input())

print(_tree_)
# Baekjoon Online Judge
# Disjoint Set
# https://www.acmicpc.net/problem/1976
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

board = [list(map(int, input().split())) for _ in range(N)]

trip_plan = list(map(int, input().split()))

_list_ = [i for i in range(N)]

for start_node in range(N):
    for end_node in range(N):
        if board[start_node][end_node] == 1:
            union(start_node, end_node)

# print(_list_)

if M == 0 or M == 1:
    print("YES")
    exit()

# 같은 그룹인지 확인
for i in range(1, M):
    if _list_[trip_plan[i] - 1] != _list_[trip_plan[i - 1] - 1]:
        print("NO")
        exit()

print("YES")

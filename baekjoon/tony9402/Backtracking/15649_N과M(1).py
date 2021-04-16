# Baekjoon Online Judge
# Backtracking
# https://www.acmicpc.net/problem/15649
# 출처 : https://github.com/tony9402/baekjoon

import sys


def backtracking(_list_):

    global answer

    if len(_list_) == M:
        answer.append(_list_)
        return

    for num in range(1, N + 1):
        if visited[num] != 1:
            visited[num] = 1

            tmp = _list_[:]
            tmp.append(num)

            backtracking(tmp)
            visited[num] = 0


input = sys.stdin.readline

N, M = map(int, input().split())

visited = [0] * (N + 1)
answer = []

backtracking([])

for lst in answer:
    print(' '.join(map(str, lst)))

# Baekjoon Online Judge
# Backtracking
# https://www.acmicpc.net/problem/15650
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline


# start - 오름차순을 위한 수열 시작 숫자
def backtracking(_list_, start):

    global answer

    if len(_list_) == M:
        answer.append(_list_)
        return

    for num in range(start, N + 1):
        if visited[num] != 1:

            visited[num] = 1
            tmp = _list_[:]
            tmp.append(num)

            backtracking(tmp, num)

            visited[num] = 0


N, M = map(int, input().split())

visited = [0] * (N + 1)
answer = []

backtracking([], 1)

for lst in answer:
    print(' '.join(map(str, lst)))

# Baekjoon Online Judge
# Two Pointers
# https://www.acmicpc.net/problem/11659
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num_list = list(map(int, input().split()))
_list_ = [0] * N

# 앞에서부터의 합
_list_[0] = num_list[0]
for i in range(1, N):
    _list_[i] = _list_[i - 1] + num_list[i]

for _ in range(M):

    i, j = map(int, input().split())
    i, j = i - 1, j - 1

    if i == 0:
        answer = _list_[j]
    elif i == j:
        answer = num_list[i]
    else:
        answer = _list_[j] - _list_[i - 1]

    print(answer)

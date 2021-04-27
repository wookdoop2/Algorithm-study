# Baekjoon Online Judge
# Trie
# https://www.acmicpc.net/problem/14425
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S = []


for _ in range(N):
    S.append(input())

answer = 0

for _ in range(M):

    _string_ = input()

    if _string_ in S:
        answer += 1

print(answer)

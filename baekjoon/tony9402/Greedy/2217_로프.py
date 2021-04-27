# Baekjoon Online Judge
# Greedy
# https://www.acmicpc.net/problem/2217
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

N = int(input())

rope_list = []
for _ in range(N):
    rope_list.append(int(input()))
rope_list.sort()

answer = [0] * N

for i in range(N):
    answer[i] = rope_list[i] * (N - i)

print(max(answer))

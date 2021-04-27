# Baekjoon Online Judge
# Math
# https://www.acmicpc.net/problem/2745
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

NOTATION = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B = map(str, input().split())

answer = 0

new_N = list(reversed(N))

for i in range(len(N)):
    answer += NOTATION.index(new_N[i]) * (int(B) ** i)

print(answer)

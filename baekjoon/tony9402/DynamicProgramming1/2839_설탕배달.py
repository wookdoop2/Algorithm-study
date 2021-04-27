# Baekjoon Online Judge
# Dynamic Programming 1
# https://www.acmicpc.net/problem/2839
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

N = int(input())

answer = 0

while N >= 0:
    if N % 5 == 0:
        answer += N // 5
        print(answer)
        exit()
    else:
        N -= 3
        answer += 1

print(-1)



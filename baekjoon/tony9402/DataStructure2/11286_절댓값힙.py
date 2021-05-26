# Baekjoon Online Judge
# Data Structure 2
# https://www.acmicpc.net/problem/11286
# 출처 : https://github.com/tony9402/baekjoon

import sys
import heapq

input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    num = int(input())

    if num != 0:
        heapq.heappush(hq, [abs(num), num])
    else:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq)[1])

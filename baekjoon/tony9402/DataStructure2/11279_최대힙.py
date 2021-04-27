# Baekjoon Online Judge
# Data Structure 2
# https://www.acmicpc.net/problem/11279
# 출처 : https://github.com/tony9402/baekjoon

import sys
import heapq

input = sys.stdin.readline

N = int(input())
hq = [[0, 0]]

for _ in range(N):

    x = int(input())

    if x == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq)[1])
    else:
        heapq.heappush(hq, [-x, x])

# Baekjoon Online Judge
# Binary Search
# https://www.acmicpc.net/problem/1789
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

S = int(input())

left = 1
right = S
answer = 0

while left < right:

    # print(left, right)

    mid = (left + right) // 2

    if mid * (mid + 1) // 2 > S:
        right = mid - 1
    else:
        answer = mid
        left = mid + 1

print(answer)


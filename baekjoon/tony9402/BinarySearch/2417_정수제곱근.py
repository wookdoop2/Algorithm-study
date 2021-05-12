# Baekjoon Online Judge
# Binary Search
# https://www.acmicpc.net/problem/2417
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

n = int(input())

# 제곱근이 소수점인 경우 (제곱근 + 1)
if n ** 0.5 % 1 != 0:
    print(int(n ** 0.5) + 1)
else:
    print(int(n ** 0.5))

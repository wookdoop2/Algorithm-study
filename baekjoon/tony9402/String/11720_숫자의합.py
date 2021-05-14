# Baekjoon Online Judge
# String
# https://www.acmicpc.net/problem/11720
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

N = int(input())

num_string = input().rstrip()

answer = 0

for num in num_string:
    answer += int(num)

print(answer)

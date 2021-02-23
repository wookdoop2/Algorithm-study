# Baekjoon Online Judge
# 알고리즘 기초 1 - Brute Force
# https://www.acmicpc.net/problem/2309
import sys

a = [int(input()) for _ in range(9)]

a.sort()
total = sum(a)

for i in range(0, 9):
    for j in range(i + 1, 9):
        if total - (a[i] + a[j]) == 100:
            for k in range(0, 9):
                if i == k or j == k:
                    continue
                print(a[k])
            sys.exit()

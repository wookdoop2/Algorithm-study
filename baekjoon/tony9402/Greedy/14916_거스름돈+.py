# Baekjoon Online Judge
# Data Structure
# https://www.acmicpc.net/problem/14916
# 출처 : https://github.com/tony9402/baekjoon

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# num5, n = divmod(n, 5)
#
# if n == 0:
#     print(num5)
#     exit()
#
# while n > 0:
#
#     num5 -= 1
#     n += 5

import sys

changes = [0 for _ in range(100001)]

changes[2] = 1
changes[4] = 2
changes[5] = 1

target = int(sys.stdin.readline().rstrip())

for i in range(6, 100001):

    if changes[i - 5] != 0 and changes[i - 2] != 0:
        changes[i] = min(changes[i - 5] + 1, changes[i - 2] + 1)
    elif changes[i - 5] != 0:
        changes[i] = changes[i - 5] + 1
    elif changes[i - 2] != 0:
        changes[i] = changes[i - 2] + 1

if changes[target] == 0:
    print(-1)
else:
    print(changes[target])



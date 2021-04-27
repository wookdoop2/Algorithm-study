# Baekjoon Online Judge
# Data Structure
# https://www.acmicpc.net/problem/10828
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):

    order = input().split()

    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(-1))
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])


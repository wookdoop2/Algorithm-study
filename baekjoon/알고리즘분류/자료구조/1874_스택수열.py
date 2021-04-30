# Baekjoon Online Judge
# Data Structure
# https://www.acmicpc.net/problem/1874

import sys

input = sys.stdin.readline

n = int(input())
stack = []
answer = []

tmp = 0
check = 0

for count in range(n):
    num = int(input())

    while tmp < num:
        tmp += 1
        stack.append(tmp)
        answer.append('+')

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        check = 1
        break

if check == 1:
    print("NO")
    exit()
else:
    print('\n'.join(answer))

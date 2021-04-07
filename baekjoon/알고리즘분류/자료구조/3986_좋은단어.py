# Baekjoon Online Judge
# Data Structure
# https://www.acmicpc.net/problem/3986

from collections import deque

N = int(input())
answer = 0

for _ in range(N):
    input_list = deque(input())

    stack_list = [input_list.popleft()]
    while input_list:
        c = input_list.popleft()
        if len(stack_list) > 0 and stack_list[-1] == c:
            stack_list.pop()
        else:
            stack_list.append(c)

    if len(stack_list) == 0:
        answer += 1

print(answer)

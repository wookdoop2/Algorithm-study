# Baekjoon Online Judge
# Data Structure
# https://www.acmicpc.net/problem/9012
from collections import deque

T = int(input())

for _ in range(T):

    input_list = deque(input())

    stack_list = [input_list.popleft()]

    while input_list:
        c = input_list.popleft()

        # stack에 값이 있고 stack 끝이 '(', 들어오는 값이 ')'이면 stack pop
        if len(stack_list) > 0 and stack_list[-1] == '(' and c == ')':
            stack_list.pop()
        else:   # stack이 비어있거나 끝이 '(', 들어오는 값이 ')'가 아니면 stack push
            stack_list.append(c)

    if len(stack_list) == 0:
        print("YES")
    else:
        print("NO")

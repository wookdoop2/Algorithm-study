# Baekjoon Online Judge
# Data Structure
# https://www.acmicpc.net/problem/1158
# 출처 : https://github.com/tony9402/baekjoon

from collections import deque

N, K = map(int, input().split())

_list_ = deque(list(range(1, N + 1)))
answer = []

# 덱 회전시킴
while _list_:

    for _ in range(K - 1):
        _list_.append(_list_.popleft())

    answer.append(_list_.popleft())

print('<' + ', '.join(map(str, answer)) + '>')

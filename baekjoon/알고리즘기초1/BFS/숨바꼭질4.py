# Baekjoon Online Judge
# BFS
# https://www.acmicpc.net/problem/13913
from collections import deque


def go(n, m):
    if n != m:
        go(n, route[m])
    print(m, end=' ')


start, end = map(int, input().split())
max_num = 200000
check = [0] * (max_num + 1)
count = [0] * (max_num + 1)
route = [0] * (max_num + 1)
_list_ = deque()

check[start] = 1
_list_.append(start)

while len(_list_) != 0:

    now = _list_.popleft()

    if 0 <= now - 1 <= max_num and check[now - 1] == 0:
        _list_.append(now - 1)
        count[now - 1] = count[now] + 1
        route[now - 1] = now
        check[now - 1] = 1

    if 0 <= now + 1 <= max_num and check[now + 1] == 0:
        _list_.append(now + 1)
        count[now + 1] = count[now] + 1
        route[now + 1] = now
        check[now + 1] = 1

    if 0 <= now * 2 <= max_num and check[now * 2] == 0:
        _list_.append(now * 2)
        count[now * 2] = count[now] + 1
        route[now * 2] = now
        check[now * 2] = 1

    # 시간 초과
    # if end in _list_:
    #     break

print(count[end])
go(start, end)

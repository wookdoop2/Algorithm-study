# Baekjoon Online Judge
# BFS
# https://www.acmicpc.net/problem/1697
start, end = input().split()
max_num = 100000
check = [0] * max_num
_list_ = []

check[start] = 1
_list_.append(start)

while len(_list_) !=0:
    now = _list_[-1]

    if now - 1 >= 0:
        if check[now - 1] == 0:
            _list_.append(now - 1)
            check[now - 1] = 1

    if now + 1 <= max_num:
        if check[now + 1] == 0:
            _list_.append(now + 1)
            check[now + 1] = 1

    if now * 2 <= max_num:
        if check[now * 2] == 0:
            _list_.append(now * 2)
            check[now * 2] = 1

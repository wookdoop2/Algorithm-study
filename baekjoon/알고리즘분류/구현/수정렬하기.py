# Baekjoon Online Judge
# Simulation
# https://www.acmicpc.net/problem/2750
count = int(input())

_list_ = []

for i in range(count):
    _list_.append(int(input()))

_list_ = sorted(_list_)

for i in _list_:
    print(i)
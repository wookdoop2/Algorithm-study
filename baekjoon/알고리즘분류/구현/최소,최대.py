# Baekjoon Online Judge
# Simulation
# https://www.acmicpc.net/problem/10818
count = int(input())
_list_ = list(map(int, input().split()))

min_num = 1000000
max_num = -1000000

for i in _list_:

    if min_num > i:
        min_num = i

    if max_num < i:
        max_num = i

print(min_num, max_num)

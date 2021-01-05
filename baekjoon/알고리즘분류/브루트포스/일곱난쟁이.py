# Baekjoon Online Judge
# Brute Force
# https://www.acmicpc.net/problem/2309
from itertools import permutations

_list_ = []
for _ in range(9):
    _list_.append(int(input()))

permutation = list(permutations(_list_, 7))
answer = []

for i in permutation:
    if sum(i) == 100:
        answer = sorted(i)
        break

for i in answer:
    print(i, end=' ')

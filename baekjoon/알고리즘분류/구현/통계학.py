# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/2108
from collections import Counter
import sys

N = int(input())
_list_ = [int(input()) for _ in range(N)]
_list_.sort()

# 1
print(round(sum(_list_) / N))

if N == 1:
    print(_list_[0])
    print(_list_[0])
    print(0)
    sys.exit()

# 2
print(_list_[N // 2])

# 3
count_list = Counter(_list_).most_common()
num0, count0 = count_list[0]
num1, count1 = count_list[1]
if count0 > count1:
    print(num0)
else:
    print(num1)

# 4
print(_list_[-1] - _list_[0])

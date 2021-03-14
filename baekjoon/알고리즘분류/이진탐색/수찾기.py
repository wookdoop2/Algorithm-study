# Baekjoon Online Judge
# Binary Search
# https://www.acmicpc.net/problem/1920
import bisect

N = int(input())
_list_ = list(map(int, input().split()))
_list_.sort()
M = int(input())
_another_list_ = list(map(int, input().split()))

# middle_num = _list_[len(_list_) // 2]

# print(_list_)
# print(_another_list_)

for i in _another_list_:
    idx = bisect.bisect_left(_list_, i)

    if idx < len(_list_) and i == _list_[idx]:  # and 조건문 순서 주의
        print(1)
    else:
        print(0)

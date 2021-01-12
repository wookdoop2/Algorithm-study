# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/2163
_list_ = [0] * 301  # 1 * n 모양의 초콜릿을 1 * 1 모양으로 만들기 위한 횟수
for i in range(2, 301):
    _list_[i] = i - 1

N, M = map(int, input().split())

print(_list_[N] + N * _list_[M])

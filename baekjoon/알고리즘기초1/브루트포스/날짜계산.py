# Baekjoon Online Judge
# 알고리즘 기초 1 - Brute Force
# https://www.acmicpc.net/problem/1476
import sys

E, S, M = map(int, input().split())
_E_, _S_, _M_ = 1, 1, 1
E_count, S_count, M_count = 1, 1, 1

for i in range(15 * 28 * 19):

    if _E_ == E and _S_ == S and _M_ == M:
        print(i + 1)
        sys.exit()

    E_count += 1
    _E_ += 1

    S_count += 1
    _S_ += 1

    M_count += 1
    _M_ += 1

    if E_count > 15:
        _E_ = 1
        E_count = 1

    if S_count > 28:
        _S_ = 1
        S_count = 1

    if M_count > 19:
        _M_ = 1
        M_count = 1

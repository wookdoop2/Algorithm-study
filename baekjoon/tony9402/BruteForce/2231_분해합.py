# Baekjoon Online Judge
# Brute Force
# https://www.acmicpc.net/problem/2231
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline
MAX = 1000000

N = int(input())

constructor = 1
answer = MAX
while constructor < N:

    tmp = constructor

    new_tmp = str(tmp)
    # 분해합 구하기
    for i in range(len(new_tmp)):
        tmp += int(new_tmp[i:i+1])

    # 분해합을 구했을 때 N인 경우 생성자가 되므로 answer에 넣어준다 (최솟값)
    if tmp == N and constructor <= answer:
        answer = constructor

    constructor += 1

if answer == MAX:
    print(0)
else:
    print(answer)

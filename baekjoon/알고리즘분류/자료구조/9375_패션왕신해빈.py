# Baekjoon Online Judge
# Data Structure
# https://www.acmicpc.net/problem/9375

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    clothes = dict()

    n = int(input())

    if n == 0:
        print(0)
        continue

    # 의상 정보 딕셔너리화
    # 안입는 경우도 각 옷 종류마다 넣어준다
    for _ in range(n):
        cloth_name, key = map(str, input().rstrip().split())
        if key not in clothes.keys():
            clothes[key] = ['', cloth_name]
        else:
            clothes[key].append(cloth_name)

    answer = 1

    # 조합 계산
    for key in clothes.keys():
        answer *= len(clothes[key])

    print(answer - 1)

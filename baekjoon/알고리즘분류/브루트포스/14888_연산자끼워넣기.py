# Baekjoon Online Judge
# Brute Force
# https://www.acmicpc.net/problem/14888

import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

num_list = list(map(int, input().split()))
_list_ = list(map(int, input().split()))
operator_list = []

# 연산자의 갯수에 따른 연산자 리스트 생성
# 2 1 1 1 -> ['+', '+', '-', '*', '//']
for i in range(4):
    if i == 0:
        for _ in range(_list_[i]):
            operator_list.append('+')
    elif i == 1:
        for _ in range(_list_[i]):
            operator_list.append('-')
    elif i == 2:
        for _ in range(_list_[i]):
            operator_list.append('*')
    else:
        for _ in range(_list_[i]):
            operator_list.append('//')

# 최댓값 최솟값 초기화
max_answer = -1e9
min_answer = 1e9

# 중복 제거
final_permutations = set(permutations(operator_list, N - 1))

for comb in final_permutations:

    front = num_list[0]
    idx = 1

    # 계산
    for i in range(N - 1):
        if comb[i] == '+':
            front = front + num_list[idx]
            idx += 1
        elif comb[i] == '-':
            front = front - num_list[idx]
            idx += 1
        elif comb[i] == '*':
            front = front * num_list[idx]
            idx += 1
        else:
            if front < 0:  # 앞에 있는 피연산자가 음수일 때
                front = -(abs(front) // num_list[idx])
            else:
                front = front // num_list[idx]
            idx += 1

    max_answer = max(max_answer, front)
    min_answer = min(min_answer, front)

print(max_answer)
print(min_answer)

# Baekjoon Online Judge
# Topological Sorting
# https://www.acmicpc.net/problem/14567
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

_list_ = [list(map(int, input().split())) for _ in range(M)]

# B 과목을 기준으로 정렬
_list_ = sorted(_list_, key=lambda x: x[1])

# 과목마다 1로 초기화
answer = [1] * (N + 1)

for i in range(M):
    A, B = _list_[i]

    if answer[B] > answer[A]:
        continue
    else:  # 선수과목을 듣고 들어야 하기 때문에 (해당 과목을 듣는 학기 = 선수과목 학기 수 + 1)
        answer[B] = answer[A] + 1

    # print(answer)

print(' '.join(list(map(str, answer[1:]))))

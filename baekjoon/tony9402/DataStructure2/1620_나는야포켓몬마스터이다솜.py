# Baekjoon Online Judge
# Data Structure 2
# https://www.acmicpc.net/problem/1620
# 출처 : https://github.com/tony9402/baekjoon

import sys

N, M = map(int, input().split())

input = sys.stdin.readline

pokemon_dict_num = {}
pokemon_list_name = []

for i in range(1, N + 1):

    pokemon = input().rstrip()  # 개행 문자 처리 필수
    pokemon_dict_num[pokemon] = str(i)
    pokemon_list_name.append(pokemon)

for _ in range(M):

    quiz = input().rstrip()  # 개행 문자 처리 필수

    if quiz.isdigit():
        print(pokemon_list_name[int(quiz) - 1])
    else:
        print(pokemon_dict_num[quiz])

# 시간 초과
# for i in range(1, N + 1):
#     pokemon_dict[str(i)] = input()
#
# for _ in range(M):
#
#     quiz = input()
#
#     if quiz.isdigit():
#         print(pokemon_dict[quiz])
#     else:
#         for idx in pokemon_dict.keys():
#             if pokemon_dict[idx] == quiz:
#                 print(idx)

# Baekjoon Online Judge
# Brute Force
# https://www.acmicpc.net/problem/2798
from itertools import combinations

count, result = map(int, input().split())
card_list = list(map(int, input().split()))

com_list = list(combinations(card_list, 3))

answer = 0
for i in range(len(com_list)):
    # print(sum(com_list[i]))
    if answer < sum(com_list[i]) <= result:
        answer = sum(com_list[i])

print(answer)


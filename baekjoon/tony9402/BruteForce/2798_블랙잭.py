import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

card_list = list(map(int, input().split()))

answer = 0

for combination in list(combinations(card_list, 3)):
    if answer <= sum(combination) <= M:
        answer = sum(combination)

print(answer)

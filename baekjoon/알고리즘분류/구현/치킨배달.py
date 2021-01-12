# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/15686
from itertools import combinations


def cal_chicken_distance(p1, p2):

    min_num = 9999
    for x in range(len(p2)):
        min_num = min(min_num, abs(p1[0] - p2[x][0]) + abs(p1[1] - p2[x][1]))

    return min_num


N, M = map(int, input().split())
house_point = []
chicken_point = []
for i in range(N):
    _list_ = list(map(int, input().split()))
    for j in range(N):
        if _list_[j] == 1:
            house_point.append([i + 1, j + 1])
        if _list_[j] == 2:
            chicken_point.append([i + 1, j + 1])

new_chicken_point = list(combinations(chicken_point, M))

answer = 9999
for i in range(len(new_chicken_point)):
    chicken_distance = 0
    for j in range(len(house_point)):
        chicken_distance += cal_chicken_distance(house_point[j], new_chicken_point[i])
    answer = min(answer, chicken_distance)

print(answer)

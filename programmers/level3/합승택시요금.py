# Programmers
# level 3
# https://programmers.co.kr/learn/courses/30/lessons/72413
# 2021 KAKAO BLIND RECRUITMENT
import heapq
import math


def solution(n, s, a, b, fares):
    answer = math.inf

    s, a, b = s - 1, a - 1, b - 1
    inf = math.inf  # 무한대값으로 초기화
    matrix = [[inf for i in range(n)] for j in range(n)]

    for fare in fares:  # fares 배열 값 삽입
        matrix[fare[0] - 1][fare[1] - 1] = fare[2]
        matrix[fare[1] - 1][fare[0] - 1] = fare[2]

    answer_list = []

    for start in range(n):
        distance = [inf] * n
        distance[start] = 0

        queue = []
        heapq.heappush(queue, [start, distance[start]])

        while queue:
            current_node, current_distance = heapq.heappop(queue)

            if distance[current_node] < current_distance:
                continue

            for adjacent, weight in enumerate(matrix[current_node]):
                d = current_distance + weight

                if d < distance[adjacent]:
                    distance[adjacent] = d
                    heapq.heappush(queue, [adjacent, d])

        answer_list.append(distance)

    # print(answer_list)

    for i in range(n):
        answer = min(answer, answer_list[s][i] + answer_list[i][a] + answer_list[i][b])

    return answer
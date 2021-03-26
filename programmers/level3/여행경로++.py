# Programmers
# level 3
# 깊이/너비 우선 탐색(DFS/BFS)
# https://programmers.co.kr/learn/courses/30/lessons/43164


def process(air_lines):
    _list_ = ["ICN"]
    route = []

    while _list_:

        top = _list_[-1]

        if top not in air_lines.keys() or len(air_lines[top]) == 0:
            route.append(_list_.pop())
        else:
            _list_.append(air_lines[top][-1])
            air_lines[top] = air_lines[top][:-1]

    return route[::-1]


def solution(tickets):
    air_lines = dict()

    for departure, destination in tickets:
        if departure not in air_lines.keys():
            air_lines[departure] = [destination]
        else:
            air_lines[departure].append(destination)

    for key in air_lines.keys():
        air_lines[key].sort(reverse=True)

    # print(air_lines)

    return process(air_lines)

# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/43162
# 탐욕법(Greedy)
def solution(routes):
    answer = 0

    sorted_routes = sorted(routes, key=lambda route: route[1])
    # print(sorted_routes)

    camera_location = sorted_routes[0][1]
    answer += 1

    for i in range(1, len(sorted_routes)):
        if sorted_routes[i][0] <= camera_location:
            continue
        camera_location = sorted_routes[i][1]
        answer += 1

    return answer

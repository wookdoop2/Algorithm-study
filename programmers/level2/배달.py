# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/12978
# Summmer/Winter Coding(~2018)
import heapq


def solution(N, road, K):

    MAX = 5000001
    town_board = [[MAX] * (N + 1) for _ in range(N + 1)]

    for start, end, time in road:
        if town_board[start][end] > time:  # 시간이 더 적게 소모되는 도로가 있다면 그 도로 시간으로 업데이트
            town_board[start][end] = time
        if town_board[end][start] > time:
            town_board[end][start] = time

    queue = []
    distance = [MAX] * (N + 1)
    distance[1] = 0
    heapq.heappush(queue, [0, 1])

    # for i in range(N + 1):
    #     print(town_board[i])

    # 다익스트라 알고리즘
    while queue:

        current_distance, current_node = heapq.heappop(queue)

        for adjacent, weight in enumerate(town_board[current_node]):
            d = current_distance + weight
            if d < distance[adjacent]:
                distance[adjacent] = d
                heapq.heappush(queue, [d, adjacent])

    answer = 0
    for time in distance:
        if time <= K:
            answer += 1

    return answer


solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)
solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)
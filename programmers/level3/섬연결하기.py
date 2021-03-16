# Programmers
# level 3
# https://programmers.co.kr/learn/courses/30/lessons/42861
# 탐욕법(Greedy)
def solution(n, costs):
    answer = 0

    costs.sort(key=lambda x: x[2])
    history = set()

    for i in range(len(costs)):

        if costs[i][0] in history and costs[i][1] in history:
            continue

        if costs[i][0] in history or costs[i][1] in history:
            history.add(costs[i][0])
            history.add(costs[i][1])
            answer += costs[i][2]

        if len(history) == n:
            return answer

    return answer


solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]])

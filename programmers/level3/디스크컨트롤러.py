# Programmers
# level 3
# https://programmers.co.kr/learn/courses/30/lessons/42627
# 힙(Heap)
import heapq


def solution(jobs):
    answer = 0
    current_time = 0
    start = -1
    count = 0

    queue = []

    while count != len(jobs):
        for job in jobs:
            if start < job[0] <= current_time:  # 현재 시점에서 처리할 수 있는 작업
                heapq.heappush(queue, [job[1], job[0]])

        if len(queue) > 0:
            t, s = heapq.heappop(queue)  # 작업 소요 시간이 작은 일 먼저 수행
            start = current_time
            current_time += t
            answer += current_time - s
            count += 1

        else:   # 현재 시점에서 처리할 수 있는 작업이 없으면 현재 시점 1초씩 증가
            current_time += 1

    return int(answer/count)


solution([[0, 3], [1, 9], [2, 6]])

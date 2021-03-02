# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/42626
# 힙(Heap)
import heapq


def solution(scoville, K):
    scoville.sort()
    answer = 0
    check = 0

    heapq.heapify(scoville)
    while scoville[0] < K:
        num1 = heapq.heappop(scoville)
        num2 = heapq.heappop(scoville)

        num3 = num1 + (num2 * 2)
        heapq.heappush(scoville, num3)

        answer += 1

        if len(scoville) == 1 and scoville[0] < K:
            check = 1
            break

    if check == 0:
        return answer
    else:
        return -1

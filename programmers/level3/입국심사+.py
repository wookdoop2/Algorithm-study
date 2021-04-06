# Programmers
# level 3
# 이진탐색
# https://programmers.co.kr/learn/courses/30/lessons/43238
def solution(n, times):

    left = 0
    answer = right = max(times) * n  # 모든 사람이 가장 오래걸리는 심사관에게 심사받을 때

    while left <= right:

        person_sum = 0  # 심사 처리 수

        mid = (left + right) // 2   # 임의의 총 심사 시간

        # 각 심사대에 mid만큼의 시간이 주어졌을 때 처리할 수 있는 사람 수
        # 모두 합해서 목표 심사 인원과 비교
        for time in times:
            person_sum += mid // time

        if person_sum < n:  # mid 시간동안 처리한 심사 인원 수가 목표 심사 인원보다 적을 때 -> left = mid + 1
            left = mid + 1
        else:   # mid 시간동안 처리한 심사 인원 수가 목표 심사 인원보다 클 때 -> right = mid - 1
            right = mid - 1

            if mid <= answer:   # 이전에 저장한 총 심사 시간보다 작은 시간이 걸리는 경우 다시 저장 (최솟값)
                answer = mid

    #         print(left)
    #         print(right)
    #         print(person_sum)
    #         print(answer)
    #         print()

    return answer

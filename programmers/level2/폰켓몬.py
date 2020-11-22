# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/1845
# 찾아라 프로그래밍 마에스터
def solution(nums):
    answer = 0

    new_nums = list(set(nums))
    # print(new_nums)

    for i in new_nums:
        if answer < len(nums) // 2:
            answer += 1

    return answer

# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/12977
# Summer/Winter Coding(~2018)
from itertools import combinations


def is_prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


def solution(nums):
    answer = 0

    nums = list(combinations(nums, 3))

    for i in nums:
        if is_prime_number(sum(i)) == 1:
            answer += 1

    return answer

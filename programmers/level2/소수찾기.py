# Programmers
# level 2
# Brute Force
# Permutation, Searching prime number
# https://programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations


def solution(numbers):
    answer = 0
    _list_ = []
    numbers = list(numbers)

    # permutation
    for i in range(1, len(numbers) + 1):
        permute = list(permutations(numbers, i))
        for j in range(len(permute)):
            _list_.append(int(''.join(list(permute[j]))))

    # check prime number
    for i in set(_list_):
        not_prime_check = 0
        if i == 0 or i == 1:
            continue
        for j in range(2, i - 1):
            if i % j == 0:
                not_prime_check = 1
                break

        if not_prime_check == 0:
            answer += 1

    return answer

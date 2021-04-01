# SW Expert Academy
# Difficulty 3

from itertools import combinations

T = int(input())

for test_case in range(T):
    N, K = map(int, input().split())

    A = list(map(int, input().split()))

    answer = 0

    for i in range(1, N + 1):
        for comb in combinations(A, i):
            if sum(comb) == K:
                answer += 1

    print("#{} {}".format(test_case + 1, answer))

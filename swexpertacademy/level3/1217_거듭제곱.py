# SW Expert Academy
# Difficulty 3


def multi(n, m):

    if m == 0:
        return 1

    return multi(n, m - 1) * n


for test_case in range(1, 11):
    t = int(input())
    N, M = map(int, input().split())

    print("#{} {}".format(test_case, multi(N, M)))
    # print("#{} {}".format(test_case, N ** M))

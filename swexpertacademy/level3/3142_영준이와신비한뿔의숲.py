# SW Expert Academy
# Difficulty 3

T = int(input())

for test_case in range(T):

    n, m = map(int, input().split())

    _list_ = []

    for i in range(m + 1):
        _list_.append([i, m - i])

    for uni, twin in _list_:
        if (2 * uni) + twin == n:
            print("#{} {} {}".format(test_case + 1, twin, uni))

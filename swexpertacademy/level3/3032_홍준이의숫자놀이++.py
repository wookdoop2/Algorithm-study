# SW Expert Academy
# Difficulty 3


def extended_euclid(r1, r2, s1, s2, t1, t2):
    q, r = divmod(r1, r2)
    s = s1 - s2 * q
    t = t1 - t2 * q

    if r == 0:
        return s2, t2
    else:
        return extended_euclid(r2, r, s2, s, t2, t)


T = int(input())

for test_case in range(T):

    A, B = map(int, input().split())

    # extended_euclid(r1, r2, s1, s2, t1, t2)
    if A > B:
        x, y = extended_euclid(A, B, 1, 0, 0, 1)
        print("#{} {} {}".format(test_case + 1, x, y))
    else:
        x, y = extended_euclid(B, A, 1, 0, 0, 1)
        print("#{} {} {}".format(test_case + 1, y, x))

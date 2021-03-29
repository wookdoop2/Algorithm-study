# SW Expert Academy
# Difficulty 3

import math


def is_prime_number(x):
    for num in range(2, int(math.sqrt(x)) + 1):
        if x % num == 0:
            return False

    return True


_list_ = []

for i in range(2, 10 ** 6 + 1):
    if is_prime_number(i):
        _list_.append(i)

for n in _list_:
    print(n, end=' ')

# SW Expert Academy
# Difficulty 3


def power(a, b):
    if b == 0:
        return 1
    if b % 2:  # 홀수일 때
        return (power(a, b//2) ** 2 * a) % p
    else:  # 짝수일 때
        return (power(a, b//2) ** 2) % p


T = int(input())

for test_case in range(1, T + 1):
    N, R = map(int, input().split())

    fact = [1 for _ in range(N + 1)]
    p = 1234567891

    for i in range(2, N + 1):
        fact[i] = fact[i - 1] * i % p

    A = fact[N]
    B = (fact[N - R] * fact[R]) % p

    # 마지막에 mod p 수행 시 계산 시간 증가
    # (A / B) % p
    # = A * B^-1 % p
    # = A * B^p-2 % p
    # = (A % p) * (B^p-2 % p) % p

    # print("#{} {}".format(test_case, (A / B) % p))
    print("#{} {}".format(test_case, ((A % p) * (power(B, p - 2) % p)) % p))

    # child = 1
    # for i in range(R):
    #     child *= N - i
    #
    # parent = 1
    # for i in range(1, R + 1):
    #     parent *= i
    #
    # print("#{} {}".format(test_case, (child // parent) % 1234567891))

    # 시간 초과

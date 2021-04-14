# Baekjoon Online Judge
# Data Structure
# https://www.acmicpc.net/problem/9084
# 출처 : https://github.com/tony9402/baekjoon

T = int(input())

for _ in range(T):

    N = int(input())
    coin_list = list(map(int, input().split()))
    M = int(input())

    dp_list = [0] * (M + 1)

    # 1 -> 0(0 + 1) + 1
    # 2 -> 0(0 + 2) + 2
    dp_list[0] = 1

    # [1, 2]
    # 1
    # 1 -> 0 + 1
    # 3 -> 2 + 1
    # 4 -> 3 + 1
    # 5 -> 4 + 1 ...
    # 2
    # 3 -> 1(3 - 2) + 2
    # 4 -> 2(4 - 2) + 2
    # 5 -> 3(5 - 2) + 2
    # 6 -> 4(6 - 2) + 2 ...
    for coin in coin_list:

        for i in range(1, M + 1):

            if i - coin >= 0:
                dp_list[i] = dp_list[i - coin] + dp_list[i]

    print(dp_list[M])

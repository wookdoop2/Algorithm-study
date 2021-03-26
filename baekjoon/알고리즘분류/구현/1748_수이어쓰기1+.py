# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/1748
num = input()

length, answer = len(num), 0

# 1 ~ 9
# 10 ~ 99
# 100 ~ 999
# 1000 ~ 9999
# ...
for l in range(1, length):
    answer += l * (10 ** l - 10 ** (l - 1))

# 10 ** (length - 1) ~ num
answer += length * (int(num) - (10 ** (length - 1)) + 1)

print(answer)

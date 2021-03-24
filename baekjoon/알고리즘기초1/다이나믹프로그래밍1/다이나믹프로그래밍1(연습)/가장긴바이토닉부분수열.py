# Baekjoon Online Judge
# Dynamic Programming
# https://www.acmicpc.net/problem/11054
n = int(input())

cost = list(map(int, input().split()))

# case1 - 가장 긴 증가하는 부분 수열
up_list = [0] * n
up_list[0] = 1

for i in range(1, n):
    up_list[i] = 1
    for j in range(i):
        if cost[j] < cost[i] and up_list[i] < up_list[j] + 1:
            up_list[i] = up_list[j] + 1

# print(up_list)

# case2 - 가장 긴 증가하는 부분 수열 (거꾸로)
up_reversed_list = [0] * n
up_reversed_list[n - 1] = 1

for i in range(n - 2, -1, -1):
    up_reversed_list[i] = 1
    for j in range(n - 1, i, -1):
        if cost[j] < cost[i] and up_reversed_list[i] < up_reversed_list[j] + 1:
            up_reversed_list[i] = up_reversed_list[j] + 1

# print(up_reversed_list)

# 두 case를 더해서 가장 값이 큰 곳 -> 가장 긴 바이토닉 부분 수열
max_num = 0
for i in range(n):
    if max_num < up_list[i] + up_reversed_list[i]:
        max_num = up_list[i] + up_reversed_list[i]

print(max_num - 1)

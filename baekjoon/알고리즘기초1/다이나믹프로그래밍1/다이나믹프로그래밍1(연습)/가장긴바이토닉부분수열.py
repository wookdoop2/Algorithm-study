# Baekjoon Online Judge
# Dynamic Programming
# https://www.acmicpc.net/problem/11054
n = int(input())

cost = list(map(int, input().split()))

up_list = [0] * n
up_list[0] = 1

for i in range(1, n):
    up_list[i] = 1
    for j in range(i):
        if cost[j] < cost[i] and up_list[i] < up_list[j] + 1:
            up_list[i] = up_list[j] + 1

print(up_list)

down_list = [0] * n
down_list[0] = 1

for i in range(1, n):
    down_list[i] = 1
    for j in range(i):
        if cost[j] > cost[i] and down_list[i] < down_list[j] + 1:
            down_list[i] = down_list[j] + 1

print(down_list)

d = [up_list[i] + down_list[i] - 1 for i in range(n)]
print(max(d))

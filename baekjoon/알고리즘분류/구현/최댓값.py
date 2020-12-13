# Baekjoon Online Judge
# Simulation
# https://www.acmicpc.net/problem/2562
max_num = 0
max_idx = 0
for i in range(9):
    num = int(input())
    if num > max_num:
        max_num = num
        max_idx = i

print(max_num)
print(max_idx + 1)

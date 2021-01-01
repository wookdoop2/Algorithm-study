# Baekjoon Online Judge
# Simulation
# https://www.acmicpc.net/problem/2908
num0, num1 = map(str, input().split())

reversed_num0 = ''
reversed_num1 = ''

for i in range(2, -1, -1):
    reversed_num0 += str(num0[i])
    reversed_num1 += str(num1[i])

print(int(reversed_num0) if int(reversed_num0) > int(reversed_num1) else int(reversed_num1))

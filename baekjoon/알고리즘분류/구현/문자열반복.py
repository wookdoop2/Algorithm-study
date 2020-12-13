# Baekjoon Online Judge
# Simulation
# https://www.acmicpc.net/problem/2675
count = int(input())

for i in range(count):
    answer = ''
    num, strings = map(str, input().split())

    for j in strings:
        answer += (j * int(num))

    print(answer)

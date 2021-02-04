# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/1032
N = int(input())
file_name = []
for i in range(N):
    file_name.append(list(input()))

pattern = file_name[0]

for i in range(1, N):
    for j in range(len(pattern)):
        if pattern[j] != file_name[i][j]:
            pattern[j] = '?'

print(''.join(pattern))

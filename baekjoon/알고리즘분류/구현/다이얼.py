# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/5622
words = list(input())

dial = dict()
dial[2] = ['A', 'B', 'C']
dial[3] = ['D', 'E', 'F']
dial[4] = ['G', 'H', 'I']
dial[5] = ['J', 'K', 'L']
dial[6] = ['M', 'N', 'O']
dial[7] = ['P', 'Q', 'R', 'S']
dial[8] = ['T', 'U', 'V']
dial[9] = ['W', 'X', 'Y', 'Z']

answer = 0
for i in range(len(words)):
    for j in range(2, 10):
        if words[i] in dial.get(j):
            answer += j
            break

print(answer + len(words))

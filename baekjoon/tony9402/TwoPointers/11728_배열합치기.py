import sys

input = sys.stdin.readline

N, M = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_idx = 0
b_idx = 0

answer = []

while True:

    if a_list[a_idx] < b_list[b_idx]:
        answer.append(a_list[a_idx])
        a_idx += 1
    elif a_list[a_idx] > b_list[b_idx]:
        answer.append(b_list[b_idx])
        b_idx += 1
    else:
        answer.append(a_list[a_idx])
        answer.append(b_list[b_idx])
        a_idx += 1
        b_idx += 1

    if a_idx == N:
        answer.extend(b_list[b_idx:])
        break
    if b_idx == M:
        answer.extend(a_list[a_idx:])
        break

print(' '.join(list(map(str, answer))))
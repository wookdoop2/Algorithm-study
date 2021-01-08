# Baekjoon Online Judge
# Brute Force
# https://www.acmicpc.net/problem/1018
N, M = map(int, input().split())
_list_ = []
for i in range(N):
    _list_.append(list(input()))

answer = 9999
for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        count_start_b = 0
        count_start_w = 0
        for y in range(i, i + 8):
            for x in range(j, j + 8):
                if (y + x) % 2 == 0:
                    if _list_[y][x] != 'B':
                        count_start_b += 1
                    if _list_[y][x] != 'W':
                        count_start_w += 1
                else:
                    if _list_[y][x] != 'W':
                        count_start_b += 1
                    if _list_[y][x] != 'B':
                        count_start_w += 1
        answer = min(answer, count_start_b, count_start_w)

print(answer)



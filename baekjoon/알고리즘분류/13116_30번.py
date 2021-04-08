# Baekjoon Online Judge
# Graph
# https://www.acmicpc.net/problem/13116
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    A_list = [A]
    while A != 1:
        A_list.append(A // 2)
        A = A // 2

    B_list = [B]
    while B != 1:
        B_list.append(B // 2)
        B = B // 2

    answer_list = []

    for i in range(len(A_list)):
        for j in range(len(B_list)):
            if A_list[i] == B_list[j]:
                answer_list.append(A_list[i])

    print(max(answer_list) * 10)

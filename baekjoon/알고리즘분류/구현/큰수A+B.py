# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/10757
N1, N2 = map(str, input().split())

if len(N1) < len(N2):
    N1 = '0' * (len(N2) - len(N1)) + N1
elif len(N1) > len(N2):
    N2 = '0' * (len(N1) - len(N2)) + N2

answer = []

up_check = 0
for i in range(len(N1) - 1, -1, -1):

    if up_check == 0:
        sum_num = int(N1[i]) + int(N2[i])
    else:
        sum_num = int(N1[i]) + int(N2[i]) + 1

    if sum_num >= 10:
        str_num = str(sum_num)
        answer.append(str_num[1])
        up_check = 1
    else:
        str_num = str(sum_num)
        answer.append(str_num[0])
        up_check = 0

if up_check == 1:
    answer.append('1')

answer.reverse()
print(''.join(answer))

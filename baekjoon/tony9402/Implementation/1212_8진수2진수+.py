# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/1212
# 출처 : https://github.com/tony9402/baekjoon

# 8진수 -> 2진수
# 8진수(0, 1, 2, 3, 4, 5, 6, 7) -> 2진수(000, 001, 010, 011, 100, 101, 110, 100)
binary_list = ["000", "001", "010", "011", "100", "101", "110", "111"]

decimal_num = list(input())

binary_num = ''
answer = ''

for num in decimal_num:
    binary_num = binary_num + binary_list[int(num)]

for i in range(len(binary_num)):
    if binary_num[i] == '1':
        answer = binary_num[i:]
        break

if len(answer) == 0:
    print("0")
else:
    print(answer)


# 시간 초과
# 8진수 -> 10진수 -> 2진수
# NOTATION = '01'
#
#
# def power(a, b):
#     if b == 0:
#         return 1
#
#     if b % 2:  # 홀수일 때
#         return power(a, b//2) ** 2 * a
#     else:  # 짝수일 때
#         return power(a, b//2) ** 2
#
#
# def to_binary(num, base):
#     q, r = divmod(num, base)
#     n = NOTATION[r]
#
#     return (to_binary(q, base) + n) if q else n
#
#
# decimal_num = list(input())
# d = 0
#
# for i in range(len(decimal_num)):
#     d += int(decimal_num[i]) * power(8, len(decimal_num) - i - 1)
#
# print(to_binary(d, 2))

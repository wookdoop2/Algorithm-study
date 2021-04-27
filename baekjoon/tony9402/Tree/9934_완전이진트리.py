# Baekjoon Online Judge
# Tree
# https://www.acmicpc.net/problem/9934
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

K = int(input())
order_list = list(map(int, input().split()))
answer_list = [[] for _ in range(K)]

depth = K - 1

while depth != -1:

    _list_ = []

    # 짝수 인덱스의 값 저장
    for i in range(len(order_list)):
        if i % 2 == 0:
            answer_list[depth].append(order_list[i])
            _list_.append(order_list[i])

    # 짝수 인덱스의 값 삭제
    for num in _list_:
        order_list.remove(num)

    # depth - 1
    depth -= 1

for answer in answer_list:
    print(' '.join(map(str, answer)))

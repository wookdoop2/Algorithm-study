# Baekjoon Online Judge
# Dynamic Programming
# https://www.acmicpc.net/problem/9465
n = int(input())

for i in range(n):
    count = int(input())
    cost_list = []
    _list_ = [[0] * 3 for _ in range(count)]
    for j in range(2):
        cost_list.append(list(map(int, input().split())))
    # print(cost_list)
    _list_[0][1] = cost_list[0][0]
    _list_[0][2] = cost_list[1][0]
    for j in range(1, count):
        _list_[j][0] = max(_list_[j - 1][1], _list_[j - 1][2])
        _list_[j][1] = max(_list_[j - 1][0] + cost_list[0][j], _list_[j - 1][2] + cost_list[0][j])
        _list_[j][2] = max(_list_[j - 1][0] + cost_list[1][j], _list_[j - 1][1] + cost_list[1][j])
    print(max(_list_[count - 1]))

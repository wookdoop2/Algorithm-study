# Baekjoon Online Judge
# Simulation
# https://www.acmicpc.net/problem/7568
count = int(input())

_list_ = []
for i in range(count):
    _list_.append(list(map(int, input().split())))
# print(_list_)

answer = []
for i in range(len(_list_)):
    tmp = 0
    weight = _list_[i][0]
    height = _list_[i][1]
    for j in range(len(_list_)):
        if j == i:
            continue
        if weight < _list_[j][0] and height < _list_[j][1]:
            tmp += 1
    answer.append(tmp + 1)

for i in answer:
    print(i, end=' ')

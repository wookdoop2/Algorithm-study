# Baekjoon Online Judge
# Dynamic Programming
count = int(input())

cost_list = []
for i in range(count):
    input_list = list(map(int, input().split()))
    cost_list.append(input_list)

_list_ = [[0] * 3 for _ in range(count)]
_list_[0][0] = cost_list[0][0]
_list_[0][1] = cost_list[0][1]
_list_[0][2] = cost_list[0][2]

for i in range(1, count):
    _list_[i][0] = cost_list[i][0] + min(_list_[i - 1][1], _list_[i - 1][2])
    _list_[i][1] = cost_list[i][1] + min(_list_[i - 1][0], _list_[i - 1][2])
    _list_[i][2] = cost_list[i][2] + min(_list_[i - 1][0], _list_[i - 1][1])

print(min(_list_[count - 1]))

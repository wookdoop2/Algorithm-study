# Baekjoon Online Judge
# Simulation
# https://www.acmicpc.net/problem/4673
_list_ = list(range(1, 10001))

start_num = 1
while start_num <= 10000:
    num = start_num
    num_str = str(num)
    for i in range(len(num_str)):
        num = num + int(num_str[i:i+1])

    if num in _list_:
        _list_.remove(num)

    start_num += 1

for i in _list_:
    print(i)

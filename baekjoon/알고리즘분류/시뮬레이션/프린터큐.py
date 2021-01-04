# Baekjoon Online Judge
# Simulation
# https://www.acmicpc.net/problem/1966
count = int(input())

for i in range(count):
    answer = 0
    N, M = map(int, input().split())
    _list_ = list(map(int, input().split()))
    target = [0] * N
    target[M] = 1

    while True:
        if _list_[0] < max(_list_):
            _list_.append(_list_.pop(0))
            target.append(target.pop(0))
        else:
            if target[0] == 1:
                print(answer + 1)
                break
            else:
                _list_.pop(0)
                target.pop(0)
                answer += 1

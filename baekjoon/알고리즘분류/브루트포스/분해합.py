# Baekjoon Online Judge
# Brute Force
# https://www.acmicpc.net/problem/2231
num = int(input())
answer = []

constructor = 1
while constructor < num:
    _num_ = constructor
    tmp = str(constructor)

    for i in range(len(tmp)):
        _num_ += int(tmp[i:i+1])

    if _num_ == num:
        answer.append(constructor)

    constructor += 1

if len(answer) > 0:
    print(min(answer))
else:
    print("0")

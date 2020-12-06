# Baekjoon Online Judge
# Brute Force
# https://www.acmicpc.net/problem/1065
n = int(input())
answer = 0

for num in range(1, n + 1):
    _list_ = list(map(int, list(str(num))))

    if len(_list_) == 1 or len(_list_) == 2:
        answer += 1
    elif len(_list_) == 3:
        tmp0 = _list_[1] - _list_[0]
        tmp1 = _list_[2] - _list_[1]
        if tmp0 == tmp1:
            answer += 1
    else:
        continue

print(answer)

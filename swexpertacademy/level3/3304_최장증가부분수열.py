# SW Expert Academy
# Difficulty 3

case = int(input())
answer = []

for test_case_num in range(case):
    n = int(input())
    ex_list = list(map(int, input().split()))

    _list_ = [0] * n

    _list_[0] = 1

    for i in range(1, n):
        _list_[i] = 1
        for j in range(i):
            if ex_list[j] < ex_list[i] and _list_[i] > _list_[j] + 1:
                _list_[i] = _list_[j] + 1

    answer.append(max(_list_))

for i in range(len(answer)):
    print("#{} {}".format(i + 1, answer[i]))

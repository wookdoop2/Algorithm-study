# SW Expert Academy
# Difficulty 3

for test_case in range(1, 11):
    N = int(input())
    search = input()
    _list_ = list(input())

    answer = 0
    for i in range(len(_list_) - len(search) + 1):
        if ''.join(_list_[i:i + len(search)]) == search:
            answer += 1

    print("#{} {}".format(test_case, answer))

# SW Expert Academy
# Difficulty 3

case = int(input())

for test_case in range(case):
    string0, string1 = input().split()

    _list_ = [[0] * (len(string0) + 1) for _ in range(len(string1) + 1)]

    for i in range(1, len(string1) + 1):
        for j in range(1, len(string0) + 1):
            if string0[j - 1] == string1[i - 1]:
                _list_[i][j] = _list_[i - 1][j - 1] + 1
            else:
                _list_[i][j] = max(_list_[i - 1][j], _list_[i][j - 1])

    print("#{} {}".format(test_case + 1, _list_[-1][-1]))

# SW Expert Academy
# Difficulty 3

for test_case in range(int(input())):

    N, M = map(int, input().split())

    set0 = set(input().split())
    set1 = set(input().split())

    print("#{} {}".format(test_case + 1, len(set0 & set1)))

# for test_case in range(int(input())):
#     N, M = map(int, input().split())
#
#     _list_ = []
#
#     for i in range(2):
#         for j in input().split():
#             _list_.append(j)
#
#     _dict_ = Counter(_list_)
#
#     answer = []
#
#     for key in _dict_.keys():
#         if _dict_[key] == 2:
#             answer += 1
#
#     print("#{} {}".format(test_case + 1, answer))

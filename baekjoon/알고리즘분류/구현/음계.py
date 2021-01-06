# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/2920
_list_ = list(map(int, input().split()))

check = 0

for i in range(1, len(_list_)):
    if _list_[i] == _list_[i - 1] + 1:
        check += 1

    if _list_[i] == _list_[i - 1] - 1:
        check -= 1

if check == 7:
    print("ascending")
elif check == -7:
    print("descending")
else:
    print("mixed")

# if _list_ == list(range(1, 9)):
#     print("ascending")
# elif _list_ == list(range(8, 0, -1)):
#     print("descending")
# else:
#     print("mixed")

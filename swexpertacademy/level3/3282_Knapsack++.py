# SW Expert Academy
# Difficulty 3

from itertools import combinations

# 시간 초과
# T = int(input())
#
# for test_case in range(T):
#     N, K = map(int, input().split())
#
#     # 물건 종류 리스트
#     _list_ = []
#
#     for i in range(N):
#         V, C = map(int, input().split())
#         _list_.append([V, C])
#
#     # 최대 가치 계산
#     max_c = 0
#     for i in range(1, N + 1):
#         for j in list(combinations(_list_, i)):
#
#             v_sum, c_sum = 0, 0
#
#             # print(j)
#
#             for _v_, _c_ in j:
#                 v_sum += _v_
#                 c_sum += _c_
#
#             if v_sum <= K:  # 최대 부피 내의 부피합일 때
#                 if max_c < c_sum:
#                     max_c = c_sum
#
#     print("#{} {}".format(test_case + 1, max_c))

# DP
T = int(input())

for test_case in range(T):
    N, K = map(int, input().split())

    # 물건 종류 리스트
    _list_ = []

    for i in range(N):
        V, C = map(int, input().split())
        _list_.append([V, C])

    dp_list = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, K + 1):
            if _list_[i - 1][0] > j:
                dp_list[i][j] = dp_list[i - 1][j]
            else:
                dp_list[i][j] = max(dp_list[i - 1][j], dp_list[i - 1][j - _list_[i - 1][0]] + _list_[i - 1][1])

    print("#{} {}".format(test_case + 1, dp_list[-1][-1]))












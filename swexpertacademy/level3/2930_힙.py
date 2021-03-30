# SW Expert Academy
# Difficulty 3

import heapq

T = int(input())

for test_case in range(T):
    N = int(input())

    _list_ = []
    pop_list = []
    answer = []

    for _ in range(N):
        command = input().split()
        if len(command) == 2:   # 연산 1
            heapq.heappush(_list_, [-int(command[1]), int(command[1])])
        else:   # 연산 2
            if len(_list_) == 0:
                pop_list.append([-1])
            else:
                pop_list.append(heapq.heappop(_list_))

    for tmp in pop_list:
        if len(tmp) == 1:
            answer.append(-1)
        else:
            answer.append(tmp[1])

    print("#{} ".format(test_case + 1) + ' '.join(map(str, answer)))

# T = int(input())
#
# for test_case in range(T):
#     N = int(input())
#
#     answer = []
#
#     for _ in range(N):
#         op = input().split()
#
#         _list_ = deque([])
#
#         if len(op) == 2:    # 연산 2
#             num = int(op[1])
#
#             if len(_list_) == 0:
#                 _list_.append(num)
#             else:
#                 parent_node_idx = len(_list_) % 2
#                 _list_.append(num)
#
#         else:   # 연산 1
#             answer.append(_list_.popleft())

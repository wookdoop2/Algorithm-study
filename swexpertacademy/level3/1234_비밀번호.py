# SW Expert Academy
# Difficulty 3

from collections import deque

for test_case in range(1, 11):
    N, num_list = map(str, input().split())
    num_list = deque(list(num_list))

    # print(num_list)

    stack_list = [num_list.popleft()]

    while num_list:

        n = num_list.popleft()

        if len(stack_list) > 0 and stack_list[-1] == n:
            stack_list.pop()
        else:
            stack_list.append(n)

    print("#{} {}".format(test_case, ''.join(stack_list)))

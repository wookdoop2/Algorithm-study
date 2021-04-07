# SW Expert Academy
# Difficulty 3

from collections import deque

for test_case in range(1, 11):
    n = int(input())
    num_list = deque(list(map(int, input().split())))

    count = 0
    minus = 1
    while True:
        if count == 5:
            count = 0
            minus = 1
        else:
            n1 = num_list.popleft() - minus
            num_list.append(n1)

            # 0이거나 음수 나오면 0으로 바꿔주고 스탑
            if num_list[-1] <= 0:
                num_list[-1] = 0
                break

            minus += 1
            count += 1

    print("#{}".format(test_case), end=" ")
    for i in range(8):
        print("{}".format(num_list[i]), end=" ")

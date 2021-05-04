# 16065
n = int(input())
seq = list(map(int, input().split()))

start_idx = seq.index(min(seq))
answer = 0

for start_num in range(min(seq), -1, -1):

    flag = 1
    left_idx, left_tmp, left_flag = start_idx, start_num, 0
    right_idx, right_tmp, right_flag = start_idx, start_num, 0

    # 12 5 7 7 8 4
    # 0 0 0 3 4 4 0
    while True:

        if left_flag == 0:
            if left_tmp > seq[left_idx - 1]:
                break

            left_tmp = seq[left_idx - 1] - left_tmp  # 4 3
            left_idx -= 1  # 5 -> 4 -> 3

        if right_flag == 0:
            if right_tmp > seq[right_idx]:
                break

            right_tmp = seq[right_idx] - right_tmp  # 0
            right_idx += 1  # 5 -> 6

        if left_idx == 0:
            left_flag = 1

        if right_idx == n:
            right_flag = 1

        if left_flag and right_flag:
            answer += 1
            break

print(answer)

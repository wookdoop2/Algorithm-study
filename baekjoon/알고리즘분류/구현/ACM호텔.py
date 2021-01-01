# Baekjoon Online Judge
# Simulation
# https://www.acmicpc.net/problem/10250
count = int(input())

for i in range(count):
    H, W, N = map(int, input().split())
    answer_room = ''

    floor_num = 0
    room_num = 0

    for j in range(N):
        floor_num = (j % H) + 1
        if j % H == 0:
            room_num += 1

    if room_num < 10:
        answer_room = str(floor_num) + '0' + str(room_num)
    else:
        answer_room = str(floor_num) + str(room_num)

    print(answer_room)

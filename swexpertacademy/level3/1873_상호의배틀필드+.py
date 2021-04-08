# SW Expert Academy
# Difficulty 3


def direction_change(c):
    if c == 'U':
        return 1, '^'
    elif c == 'D':
        return 3, 'v'
    elif c == 'L':
        return 0, '<'
    else:
        return 2, '>'


def move(c):

    global d_idx
    global d
    global start
    global tank_map

    # 전차 방향 먼저 바꿔주고
    d_idx, c_str = direction_change(c)
    tank_map[start[0]][start[1]] = c_str

    # 해당 방향으로 갈 수 있는지 없는지 체크
    next_y = start[0] + d[d_idx][0]
    next_x = start[1] + d[d_idx][1]

    if 0 <= next_y < H and 0 <= next_x < W and tank_map[next_y][next_x] == '.':
        tank_map[start[0]][start[1]] = '.'
        tank_map[next_y][next_x] = c_str
        start = next_y, next_x


def shoot():

    global d_idx
    global d
    global start
    global tank_map

    bullet_y, bullet_x = start[0], start[1]

    while 0 <= bullet_y < H and 0 <= bullet_x < W and tank_map[bullet_y][bullet_x] != '#':

        bullet_y, bullet_x = bullet_y + d[d_idx][0], bullet_x + d[d_idx][1]

        if tank_map[bullet_y][bullet_x] == '*':
            tank_map[bullet_y][bullet_x] = '.'
            return


T = int(input())

for test_case in range(1, T + 1):
    H, W = map(int, input().split())

    tank_map = [list(map(str, input())) for _ in range(H)]
    # print(tank_map)

    N = int(input())

    command_list = list(map(str, input()))
    # print(command_list)

    # 탱크 시작 지점 찾기
    d_idx = -1
    for i in range(H):
        for j in range(W):
            _map_ = tank_map[i][j]
            if _map_ == '^':
                start = [i, j]
                d_idx = 1
            elif _map_ == 'v':
                start = [i, j]
                d_idx = 3
            elif _map_ == '<':
                start = [i, j]
                d_idx = 0
            elif _map_ == '>':
                start = [i, j]
                d_idx = 2
            else:
                continue

    # 방향 (좌, 상, 우, 하)
    d = [[0, -1], [-1, 0], [0, 1], [1, 0]]

    for command in command_list:
        # 방향 조절 및 이동
        if command == 'U' or command == 'D' or command == 'L' or command == 'R':
            move(command)
        # 포탄 발사
        else:
            shoot()

    print("#{}".format(test_case), end=' ')
    for i in range(H):
        print(''.join(tank_map[i]))

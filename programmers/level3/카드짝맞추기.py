# Programmers
# level 3
# https://programmers.co.kr/learn/courses/30/lessons/72415
# 2021 KAKAO BLIND RECRUITMENT
from itertools import permutations
from collections import deque

size = 4
myboard = [[] for _ in range(4)]
card_pos = {}
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
orders = []
INF = int(1e4)
answer = INF


# 전역 변수를 이용한 보드(myboard), 카드 2장의 위치(card_pos) 초기화
# 지우는 순서에 대한 순열(orders) 초기화
# card_pos 예시: card_pos[1] = [[0,0], [1,2]] // 카드 1은 보드의 [0,0], [1,2]에 존재
def init(board):

    global myboard, card_pos, orders

    for i in range(size):
        for j in range(size):
            if board[i][j] != 0:
                card = board[i][j]
                if card not in card_pos.keys():
                    card_pos[card] = [[i, j]]
                else:
                    card_pos[card].append([i, j])

            myboard[i].append(board[i][j])

    orders = list(permutations(list(card_pos.keys())))


def card_remove(card):

    global myboard, card_pos

    for y, x in card_pos[card]:
        myboard[y][x] = 0


def card_restore(card):

    global myboard, card_pos

    for y, x in card_pos[card]:
        myboard[y][x] = card


# 이동한 결과가 보드 범위내 있는지 판단하는 함수
def isin(y, x):
    if -1 < y < size:
        if -1 < x < size:
            return True
    return False


def ctrl_move(sp_y, sp_x, _d_):

    global myboard

    _y_, _x_ = sp_y, sp_x

    while True:
        new_y_ = _y_ + _d_[0]
        new_x_ = _x_ + _d_[1]

        if not isin(new_y_, new_x_):
            return _y_, _x_

        if myboard[new_y_][new_x_] != 0:
            return new_y_, new_x_

        _y_ = new_y_
        _x_ = new_x_


def bfs(sp_y, sp_x, ep_y, ep_x):

    global myboard

    # 맨 처음 주어진 시작점과 타겟 카드의 좌표가 같을 때
    if [sp_y, sp_x] == [ep_y, ep_x]:
        return sp_y, sp_x, 1

    queue = []
    queue = deque(queue)
    queue.append([sp_y, sp_x])

    check = [[0 for i in range(size)] for _ in range(size)]
    count = [[0 for i in range(size)] for _ in range(size)]
    check[sp_y][sp_x] = 1

    while queue:

        y, x = queue.popleft()

        for i in range(4):
            new_y = y + d[i][0]
            new_x = x + d[i][1]
            # 한칸씩 움직일 때
            if isin(new_y, new_x):
                if check[new_y][new_x] != 0:
                    check[new_y][new_x] = 1
                    count[new_y][new_x] = count[y][x] + 1
                    if [new_y, new_x] == [ep_y, ep_x]:  # 타겟 카드에 왔을 때
                        return new_y, new_x, count[new_y][new_x] + 1  # 타겟 카드 위치와 키 조작(삭제 포함) 횟수
                    queue.append([new_y, new_x])

            # ctrl 누르고 움직일 때
            new_y, new_x = ctrl_move(y, x, d[i])

            if check[new_y][new_x] != 0:
                check[new_y][new_x] = 1
                count[new_y][new_x] = count[y][x] + 1
                if [new_y, new_x] == [ep_y, ep_x]:  # 타겟 카드에 왔을 때
                    return new_y, new_x, count[new_y][new_x] + 1  # 타켓 카드 위치와 키 조작(삭제 포함) 횟수
                queue.append([new_y, new_x])

    return sp_y, sp_x, INF


def start(start_point_y, start_point_x, order_idx, card_idx, cost):

    global orders, card_pos, myboard, answer

    if card_idx == len(card_pos.keys()):
        if answer > cost:
            answer = cost
            return

    order = orders[order_idx][card_idx]
    first_card_y, first_card_x = card_pos[order][0][0], card_pos[order][0][1]
    second_card_y, second_card_x = card_pos[order][1][0], card_pos[order][1][1]

    y0, x0, cost0 = bfs(start_point_y, start_point_x, first_card_y, first_card_x)
    y1, x1, cost1 = bfs(y0, x0, second_card_y, second_card_x)

    card_remove(order)
    start(y1, x1, order_idx, card_idx + 1, cost + cost0 + cost1)
    card_restore(order)

    y0, x0, cost0 = bfs(start_point_y, start_point_x, second_card_y, second_card_x)
    y1, x1, cost1 = bfs(y0, x0, first_card_y, first_card_x)

    card_remove(order)
    start(y1, x1, order_idx, card_idx + 1, cost + cost0 + cost1)
    card_restore(order)


def solution(board, r, c):

    global answer

    init(board)

    print(myboard)
    print(card_pos)
    print(orders)

    for i in range(len(orders)):
        start(r, c, i, 0, 0)

    print(answer)
    return answer


solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0)

import sys
from collections import deque


def check(y, x):

    global answer

    country = [
        [board[y][x], board[y][x + 1]],
        [board[y + 1][x], board[y + 1][x + 1]]
    ]
    _list_ = [[0, 1], [2, 3]]
    visited = [[0, 0], [0, 0]]
    dq = deque([[0, 0]])

    while dq:

        country_y, country_x = dq.popleft()

        visited[country_y][country_x] = 1

        for d in direction:

            new_y = country_y + d[0]
            new_x = country_x + d[1]

            if 0 <= new_y <= 1 and 0 <= new_x <= 1:
                if visited[new_y][new_x] != 1 and L <= abs(country[country_y][country_x] - country[new_y][new_x]) <= R:
                    _list_[new_y][new_x] = _list_[country_y][country_x]
                    dq.append([new_y, new_x])

    # 연합의 갯수와 인구이동
    _set_ = set()
    for i in range(2):
        for j in range(2):
            _set_.add(_list_[i][j])

    if len(_set_) == 3:
        answer += 1
    elif len(_set_) == 2:
        if _set_[0] ==


input = sys.stdin.readline

N, L, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

answer = 0

for i in range(N - 1):
    for j in range(N - 1):
        check(i, j)

print(answer)
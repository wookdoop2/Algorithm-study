# Baekjoon Online Judge
# DFS
# https://www.acmicpc.net/problem/4963

import sys

input = sys.stdin.readline

# 상 우 하 좌 대각선
di = [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, -1], [-1, 1], [1, 1], [1, -1]]
sys.setrecursionlimit(10000)


def dfs(_y_, _x_):

    visited[_y_][_x_] = 1

    # 상 하 좌 우 대각선 확인
    for d in di:

        new_y, new_x = _y_ + d[0], _x_ + d[1]

        # 다음 칸이 지도 범위 안에 있고, 한 번도 들른적이 없고, 섬 일때 다시 dfs를 돌아준다
        if 0 <= new_y < h and 0 <= new_x < w and visited[new_y][new_x] != 1 and map_board[new_y][new_x] == 1:
            dfs(new_y, new_x)

    return


while True:

    w, h = map(int, input().split())

    # 입력이 0 0 이면 종료
    if w == 0 and h == 0:
        break

    # 2차원 배열 지도와 visited 리스트
    map_board = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    island_count = 0

    # 모든 지도를 순회
    for i in range(h):
        for j in range(w):

            # 한번도 들른적이 없고 섬이면 섬 count + 1을 하고 dfs 함수 시작
            if visited[i][j] != 1 and map_board[i][j] == 1:
                island_count += 1
                dfs(i, j)

    print(island_count)

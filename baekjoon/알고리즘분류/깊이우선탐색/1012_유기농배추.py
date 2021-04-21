# Baekjoon Online Judge
# DFS
# https://www.acmicpc.net/problem/1012

import sys

# 상 우 하 좌
di = [[-1, 0], [0, 1], [1, 0], [0, -1]]
sys.setrecursionlimit(10000)


def dfs(_y_, _x_):

    visited[_y_][_x_] = 1

    # 상 하 좌 우 확인
    for d in di:

        new_y, new_x = _y_ + d[0], _x_ + d[1]

        # 다음 칸이 배추밭 범위 안에 있고, 한 번도 들른적이 없고, 배추가 있을 때 다시 dfs를 돌아준다
        if 0 <= new_y <= N - 1 and 0 <= new_x <= M - 1 and visited[new_y][new_x] != 1 and latus_board[new_y][new_x] == 1:
            dfs(new_y, new_x)

    return


input = sys.stdin.readline

T = int(input())

for _ in range(T):

    M, N, K = map(int, input().split())

    latus_board = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        latus_board[y][x] = 1

    latus_bug_count = 0

    # 모든 밭을 순회
    for i in range(N):
        for j in range(M):

            # 한번도 들른적이 없고 배추가 있으면 배추벌레 count + 1을 하고 dfs 함수 시작
            if visited[i][j] != 1 and latus_board[i][j] == 1:
                latus_bug_count += 1
                dfs(i, j)

    # for i in range(N):
    #     print(latus_board[i])

    print(latus_bug_count)

# Baekjoon Online Judge
# DFS BFS
# https://www.acmicpc.net/problem/2468

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 상 우 하 좌
di = [[-1, 0], [0, 1], [1, 0], [0, -1]]


# DFS
def dfs(y, x):

    global visited
    global height

    # 방문한 곳은 1로 설정
    visited[y][x] = 1

    for d in di:
        new_y, new_x = y + d[0], x + d[1]

        # 잠긴 곳이 아니고, 방문한 적이 없고, 지역 내의 범위일 때
        if 0 <= new_y < N and 0 <= new_x < N and board[new_y][new_x] > height and visited[new_y][new_x] != 1:
            dfs(new_y, new_x)

    return


N = int(input())
board = []
answer = 1
max_height = 0
for _ in range(N):
    _list_ = list(map(int, input().split()))
    max_height = max(max_height, max(_list_))
    board.append(_list_)

# 1부터 max_height - 1까지 잠겼을 경우
for height in range(1, max_height):

    visited = [[0] * N for _ in range(N)]
    safe_region = 0

    # 물에 잠긴 곳을 1로 초기화
    # 물에 잠긴 곳과 방문한 곳을 동일하게 설정
    for i in range(N):
        for j in range(N):
            if board[i][j] <= height:
                visited[i][j] = 1

    # DFS
    for i in range(N):
        for j in range(N):
            if visited[i][j] != 1:
                dfs(i, j)
                safe_region += 1

    answer = max(answer, safe_region)

print(answer)

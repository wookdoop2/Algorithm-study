# Baekjoon Online Judge
# BFS
# https://www.acmicpc.net/problem/7569

import sys
from collections import deque

input = sys.stdin.readline

# z, y, x (상 우 하 좌 위 아래)
di = [[0, -1, 0], [0, 0, 1], [0, 1, 0], [0, 0, -1], [-1, 0, 0], [1, 0, 0]]


def bfs(_dq_):

    while _dq_:

        z, y, x = _dq_.popleft()

        for d in di:

            new_z, new_y, new_x = z + d[0], y + d[1], x + d[2]

            if 0 <= new_z < H and 0 <= new_y < N and 0 <= new_x < M and tomato_box[new_z][new_y][new_x] == 0:
                if visited[new_z][new_y][new_x] == 0:
                    _dq_.append([new_z, new_y, new_x])
                    tomato_box[new_z][new_y][new_x] = 1
                    visited[new_z][new_y][new_x] = visited[z][y][x] + 1


# 창고 안의 모든 토마토가 익었는지 안익었는지 확인하는 함수
def check():

    global tomato_box

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato_box[i][j][k] == 0:
                    return False
    return True


M, N, H = map(int, input().split())

tomato_box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

answer = 0
dq = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato_box[i][j][k] == 1 and visited[i][j][k] == 0:
                visited[i][j][k] = 1
                dq.append([i, j, k])  # 시작점 저장

bfs(dq)

if check():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                answer = max(answer, visited[i][j][k])
    print(answer - 1)
else:
    print(-1)

# Baekjoon Online Judge
# DFS
# https://www.acmicpc.net/problem/2178
from collections import deque

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input())))
check_list = [[0] * M for _ in range(N)]
cost = [[0] * M for _ in range(N)]

# 네 방향
d = [[-1, 0], [0, -1], [1, 0], [0, 1]]

# 초기화
answer = 10000
queue = deque()
queue.append([0, 0])
check_list[0][0] = 1
cost[0][0] = 1

# DFS
while queue:
    x, y = queue.popleft()

    for i in range(4):

        dx = d[i][0] + x
        dy = d[i][1] + y

        # 미로 범위 내에 있고, 한번도 안들렸고, 미로 칸이 1일 때
        if 0 <= dx < N and 0 <= dy < M and check_list[dx][dy] != 1 and board[dx][dy] != 0:
            cost[dx][dy] = cost[x][y] + board[dx][dy]
            queue.append([dx, dy])
            check_list[dx][dy] = 1

# 정답 출력
print(cost[N - 1][M - 1])

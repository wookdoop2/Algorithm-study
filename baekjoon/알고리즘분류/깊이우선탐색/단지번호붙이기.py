# Baekjoon Online Judge
# DFS
# https://www.acmicpc.net/problem/2667
# dfs 함수와 단지 수를 세기 위한 전역변수 count
def dfs(start):

    global count

    check_list[start[0]][start[1]] = 1

    for i in range(4):
        dx = d[i][0] + start[0]
        dy = d[i][1] + start[1]
        if 0 <= dx < N and 0 <= dy < N and check_list[dx][dy] != 1 and board[dx][dy] != 0:
            count += 1
            dfs([dx, dy])


N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input())))
check_list = [[0] * N for _ in range(N)]
count_list = []

d = [[-1, 0], [0, -1], [1, 0], [0, 1]]

# 모든 board를 다 돌면서 1일 경우 dfs 시작
for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and check_list[i][j] != 1:
            count = 1
            dfs([i, j])
            count_list.append(count)

print(len(count_list))
count_list.sort()
for i in count_list:
    print(i)

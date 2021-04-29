import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 상 우 하 좌
di = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def dfs(y, x, c):

    global history
    global answer

    answer = max(answer, c)
    history.add(board[y][x])

    for d in di:
        new_y, new_x = y + d[0], x + d[1]

        # 보드 범위 내에 있고, 지나온 모든 칸에 적혀 있는 알파벳 중 겹치는 것이 없을 때
        if 0 <= new_y < R and 0 <= new_x < C and board[new_y][new_x] not in history:
            dfs(new_y, new_x, c + 1)
            history.remove(board[new_y][new_x])  # backtracking

    return


R, C = map(int, input().split())

board = [list(input().rstrip()) for _ in range(R)]
history = set()  # 지나온 모든 칸의 알파벳 저장
answer = 1

# DFS
dfs(0, 0, answer)

print(answer)

# 시간초과가 떠서 PyPy3로 제출

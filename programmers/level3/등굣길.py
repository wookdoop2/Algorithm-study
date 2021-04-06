# Programmers
# level 3
# 동적 계획법(Dynamic Programming)
# https://programmers.co.kr/learn/courses/30/lessons/42898
def solution(m, n, puddles):
    answer = 0

    board = [[0] * (m + 1) for _ in range(n + 1)]
    board[1][1] = 1  # 집 위치 1로 초기화

    # 각 위치 별 최단 경로 구하기
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:   # 물에 잠긴 지역
                board[i][j] = 0
            else:
                board[i][j] = board[i - 1][j] + board[i][j - 1]

    # for i in range(n + 1):
    #     print(board[i])

    return board[-1][-1] % 1000000007

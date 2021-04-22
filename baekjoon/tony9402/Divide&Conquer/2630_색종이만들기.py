# Baekjoon Online Judge
# Divide & Conquer
# https://www.acmicpc.net/problem/2630
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline


# 시작점과 길이/2 넘겨주기
def check(start_y, start_x, n):

    global final_white_paper_count, final_blue_paper_count

    white_paper_count = 0
    blue_paper_count = 0

    # 정사각형이 모두 같은 색인지 체크
    for i in range(n):
        for j in range(n):
            if board[start_y + i][start_x + j] == 1:
                blue_paper_count += 1
            if board[start_y + i][start_x + j] == 0:
                white_paper_count += 1

    # 정사각형이 모두 파란색이면 파란색 색종이 수 + 1하고 함수 끝내기
    if blue_paper_count == n * n:
        final_blue_paper_count += 1
        return

    # 정사각형이 모두 하얀색이면 하얀색 색종이 수 + 1하고 함수 끝내기
    if white_paper_count == n * n:
        final_white_paper_count += 1
        return

    # 위의 두 조건을 모두 만족하지 않으면 시작점과 길이/2 넘겨주기
    check(start_y, start_x, n // 2)
    check(start_y, start_x + n // 2, n // 2)
    check(start_y + n // 2, start_x, n // 2)
    check(start_y + n // 2, start_x + n // 2, n // 2)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

final_white_paper_count = 0
final_blue_paper_count = 0

# 시작점과 정사각형 길이
check(0, 0, N)

print(final_white_paper_count)
print(final_blue_paper_count)

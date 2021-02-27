# Baekjoon Online Judge
# Implementation
# https://www.acmicpc.net/problem/14500
def tetro(_list_):

    shape = [
        [[0, 0], [1, 0], [2, 0], [2, 1]],
        [[0, 2], [1, 2], [1, 1], [1, 0]],
        [[0, 0], [0, 1], [1, 1], [2, 1]],
        [[1, 0], [0, 0], [0, 1], [0, 2]],
        [[0, 1], [1, 1], [2, 1], [2, 0]],
        [[0, 0], [0, 1], [0, 2], [1, 2]],
        [[0, 1], [0, 0], [1, 0], [2, 0]],
        [[0, 0], [1, 0], [1, 1], [1, 2]],

        [[0, 0], [1, 0], [1, 1], [2, 1]],
        [[1, 0], [1, 1], [0, 1], [0, 2]],
        [[0, 1], [1, 1], [1, 0], [2, 0]],
        [[0, 0], [0, 1], [1, 1], [1, 2]],

        [[0, 0], [0, 1], [0, 2], [1, 1]],
        [[0, 0], [1, 0], [2, 0], [1, 1]],
        [[1, 0], [1, 1], [1, 2], [0, 1]],
        [[0, 1], [1, 1], [2, 1], [1, 0]],

        [[0, 0], [0, 1], [0, 2], [0, 3]],
        [[0, 0], [1, 0], [2, 0], [3, 0]],
        [[0, 0], [0, 1], [1, 0], [1, 1]]
    ]

    answer = 0

    for i in range(N):
        for j in range(M):

            for m in range(len(shape)):
                sum_tetro = 0
                for n in range(4):
                    point = shape[m][n]
                    if i + point[0] > N - 1 or j + point[1] > M - 1:
                        continue
                    else:
                        sum_tetro += _list_[i + point[0]][j + point[1]]
                answer = max(answer, sum_tetro)

    return answer


N, M = map(int, input().split())
_list_ = [list(map(int, input().split())) for _ in range(N)]

print(tetro(_list_))

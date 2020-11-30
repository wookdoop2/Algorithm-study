# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/17679
# 2018 KAKAO BLINK RECRUITMENT
def solution(m, n, board):
    answer = 0

    _list_ = [[0] * n for _ in range(m)]
    for i in range(m):
        _list_[i] = list(board[i])

    while True:
        # 지워지는 블록 좌표
        delete_point = set()

        for i in range(1, m):
            for j in range(1, n):
                p0 = _list_[i - 1][j - 1]
                p1 = _list_[i - 1][j]
                p2 = _list_[i][j - 1]
                p3 = _list_[i][j]
                if p0 == p1 == p2 == p3 != '0':
                    delete_point.add((i - 1, j - 1))
                    delete_point.add((i - 1, j))
                    delete_point.add((i, j - 1))
                    delete_point.add((i, j))
        # print(delete_point)

        delete_point = list(delete_point)
        if len(delete_point) == 0:
            return answer
        else:
            answer += len(delete_point)

        # 블록 지우기
        for i in delete_point:
            _point_ = list(i)
            _list_[_point_[0]][_point_[1]] = '0'

        # print(_list_)

        for i in range(m - 1, 0, -1):
            for j in range(n):
                if _list_[i][j] == '0':
                    for k in range(i - 1, -1, -1):
                        if _list_[k][j] != '0':
                            _list_[i][j] = _list_[k][j]
                            _list_[k][j] = '0'
                            break
                        else:
                            continue
        # print(_list_)

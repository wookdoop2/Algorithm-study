# Programmers
# level 2
# Divide and Conquer
# https://programmers.co.kr/learn/courses/30/lessons/68936
# 월간 코드 챌린지 시즌 1
def solution(arr):
    answer = []

    def lets_go(start_x, start_y, length):
        tmp = arr[start_y][start_x]
        if length == 1:
            if tmp == 0:
                return [1, 0]
            else:
                return [0, 1]

        area0 = lets_go(start_x, start_y, length // 2)
        area1 = lets_go(start_x + (length // 2), start_y, length // 2)
        area2 = lets_go(start_x, start_y + (length // 2), length // 2)
        area3 = lets_go(start_x + (length // 2), start_y + (length // 2), length // 2)

        if area0 == area1 == area2 == area3 == [1, 0]:
            return area0
        elif area0 == area1 == area2 == area3 == [0, 1]:
            return area0
        else:
            return list(map(sum, zip(area0, area1, area2, area3)))

    answer = lets_go(0, 0, len(arr))

    return answer

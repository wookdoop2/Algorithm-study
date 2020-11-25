# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/68936
# 월간 코드 챌린지 시즌 1
def lets_go(start_x, start_y, length):
    area0 = lets_go(start_x, start_y, length // 2)
    area1 = lets_go(start_x + (length // 2), start_y, length // 2)
    area2 = lets_go(start_x, start_y + (length // 2), length // 2)
    area3 = lets_go(start_x + (length // 2), start_y + (length // 2), length // 2)

    if area0 == area1 == area2 == area3 == 0 or area0 == area1 == area2 == area3 == 1:
        return area0


def solution(arr):
    answer = []

    result = lets_go(0, 0, len(arr))

    return answer

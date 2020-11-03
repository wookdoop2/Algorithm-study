# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/42586
import math
def solution(progresses, speeds):
    answer = []
    days = []
    count = 1
    for i in range(len(speeds)):
        temp = (100 - progresses[i]) / speeds[i]
        days.append(math.ceil(temp))
    for i in range(1, len(days)):
        if days[i - 1] > days[i]:
            days[i] = days[i - 1]
    for i in range(1, len(days)):
        if days[i - 1] == days[i]:
            count += 1
        if days[i - 1] < days[i]:
            answer.append(count)
            count = 1
        if i == len(days) - 1:
            answer.append(count)
    return answer

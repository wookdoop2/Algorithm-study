# Programmers
# level 1
# https://programmers.co.kr/learn/courses/30/lessons/12982
# Summer/Winter Coding(~2018)
def solution(d, budget):
    answer = 0
    while True:
        answer = len(d)
        sum_num = sum(d)
        if sum_num > budget:
            index = d.index(max(d))
            d.remove(d[index])
        else:
            break
    return answer

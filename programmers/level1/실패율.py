# Programmers
# level 1
# https://programmers.co.kr/learn/courses/30/lessons/42889
# 2019 KAKAO BLIND RECRUITMENT
def solution(N, stages):
    answer = []
    fail_list = []
    temp = 0
    for i in range(1, N + 1):
        if temp == len(stages):
            fail_ = 0
            fail_list.append(fail_)
        else:
            num = stages.count(i)
            fail_ = num / (len(stages) - temp)
            fail_list.append(fail_)
            temp = temp + num

    id_list = list(range(1, N + 1))
    new_list = list(zip(fail_list, id_list))
    new_list = sorted(new_list, reverse=True, key=lambda x: x[0])

    for i in range(0, len(new_list)):
        answer.append(new_list[i][1])

    return answer

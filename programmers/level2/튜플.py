# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/64065
# 2019 카카오 개발자 겨울 인턴십
def solution(s):
    answer = []

    # Split string(s)
    s = s[2:-2].split('},{')
    s = sorted(s, key=len)

    for i in range(len(s)):
        num_list = s[i].split(',')
        for j in num_list:
            if int(j) not in answer:
                answer.append(int(j))

    return answer

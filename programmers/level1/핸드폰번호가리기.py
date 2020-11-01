# Programmers
# level 1
# https://programmers.co.kr/learn/courses/30/lessons/12948
def solution(phone_number):
    answer = ''
    # secret = phone_number[-len(phone_number):-4]
    secret = phone_number[-4:]
    length = len(phone_number) - 4
    for i in range(0, length):
        answer = answer + '*'
    answer = answer + secret
    return answer

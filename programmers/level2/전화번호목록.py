# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    answer = True

    for head_phone_number in phone_book:

        for i in phone_book:

            if head_phone_number == i or len(head_phone_number) > len(i):
                continue

            part_num = i[0:len(head_phone_number)]

            if head_phone_number == part_num:
                answer = False
                return answer

    return answer

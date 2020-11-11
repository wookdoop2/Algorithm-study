# Programmers
# level 1
# https://programmers.co.kr/learn/courses/30/lessons/42840
# Brute-force
def solution(answers):
    answer = []
    answer_ = []
    length = len(answers)
    num1 = []
    num2 = []
    num3 = []
    count1 = 0
    count2 = 0
    count3 = 0
    num1_ = [1, 2, 3, 4, 5]
    num2_ = [2, 1, 2, 3, 2, 4, 2, 5]
    num3_ = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(length):
        num1.append(num1_[i % 5])
        num2.append(num2_[i % 8])
        num3.append(num3_[i % 10])

    for i in range(length):
        if answers[i] == num1[i]:
            count1 = count1 + 1
        if answers[i] == num2[i]:
            count2 = count2 + 1
        if answers[i] == num3[i]:
            count3 = count3 + 1

    answer_.append(count1)
    answer_.append(count2)
    answer_.append(count3)

    if answer_[0] > answer_[1] and answer_[0] > answer_[2]:
        answer.append(1)
    elif answer_[1] > answer_[0] and answer_[1] > answer_[2]:
        answer.append(2)
    elif answer_[2] > answer_[0] and answer_[2] > answer_[1]:
        answer.append(3)
    elif answer_[0] == answer_[1] and answer_[1] > answer_[2]:
        answer.append(1)
        answer.append(2)
    elif answer_[1] == answer_[2] and answer_[2] > answer_[0]:
        answer.append(2)
        answer.append(3)
    elif answer_[0] == answer_[2] and answer_[2] > answer_[1]:
        answer.append(1)
        answer.append(3)
    elif answer_[0] == answer_[1] == answer_[2]:
        answer.append(1)
        answer.append(2)
        answer.append(3)
    else:
        answer.append()

    return answer
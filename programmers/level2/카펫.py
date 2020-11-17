# Programmers
# level 2
# Brute Force
# https://programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, yellow):
    answer = []

    for i in range(1, yellow + 1):

        height = i
        if yellow % i != 0:
            continue
            
        width = yellow // i

        total_brown = (height * 2) + (width * 2) + 4

        if total_brown == brown:
            answer.append(width + 2)
            answer.append(height + 2)
            return answer

# Programmers
# level 2
# Greedy
# https://programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    answer = 0
    start_index = 0
    end_index = len(people) - 1

    people = sorted(people)

    # timeout occurs when deleting a value from the list
    while True:

        if people[start_index] + people[end_index] > limit:
            answer += 1
            end_index -= 1
        else:
            answer += 1
            start_index += 1
            end_index -= 1

        if start_index > end_index:
            return answer
        elif start_index == end_index:
            return answer + 1

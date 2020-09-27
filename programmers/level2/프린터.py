def solution(priorities, location):
    answer = 0
    max_pr = max(priorities)
    while True:
        temp1 = priorities.pop(0)
        if max_pr == temp1:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            max_pr = max(priorities)
        else:
            priorities.append(temp1)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer

def solution(arr, divisor):
    answer = []
    new_list = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if len(answer) == 0:
        answer.append(-1)
        return answer
    answer.sort()
    return answer

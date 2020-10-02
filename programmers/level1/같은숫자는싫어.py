def solution(arr):
    answer = []
    length = len(arr)
    temp = -1
    for i in range(0, length):
        if arr[i] == temp:
            continue
        temp = arr[i]
        answer.append(arr[i])

    return answer

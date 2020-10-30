def solution(strings, n):
    strings = sorted(strings)
    answer = sorted(strings, key=lambda element: element[n])

    return answer

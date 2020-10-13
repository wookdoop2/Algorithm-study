# level 2
def solution(s):
    answer = ""
    msg = list(s.split(' '))

    for i in msg:
        i = i.lower()
        i = i.capitalize()
        answer += i + " "

    return answer[:-1]

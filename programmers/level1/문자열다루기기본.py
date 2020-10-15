# level 1
def solution(s):
    answer = 0
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        answer = True
    else:
        answer = False
    return answer

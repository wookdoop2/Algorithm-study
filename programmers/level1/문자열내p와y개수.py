# Programmers
# level 1
# https://programmers.co.kr/learn/courses/30/lessons/12916
from collections import Counter

def solution(s):
    answer = 0
    new_s = s.lower()
    print(Counter(new_s))
    if Counter(new_s).get('p') == Counter(new_s).get('y'):
        answer = True
    else:
        answer = False
    return answer

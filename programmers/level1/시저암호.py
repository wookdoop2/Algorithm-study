# Programmers
# level 1
# https://programmers.co.kr/learn/courses/30/lessons/12926
def solution(s, n):
    answer = ''
    s = list(s)
    for i in range(0, len(s)):
        if s[i] == ' ':
            continue
        new = ord(s[i]) + n
        if s[i].isupper() and new > ord('Z'):
            new = ord('A') + (new - (ord('Z') + 1))
        if s[i].islower() and new > ord('z'):
            new = ord('a') + (new - (ord('z') + 1))
        new = chr(new)
        s[i] = new
    answer = ''.join(s)
    return answer

# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/72410
# 2021 KAKAO BLINK RECRUITMENT
def solution(new_id):
    answer = ''

    # 1단계
    new_id = new_id.lower()

    # 2단계
    for i in new_id:
        if i.isalpha() or i.isdigit() or i == '-' or i == '_' or i == '.':
            answer += i

    # 3단계
    idx = 1
    while idx < len(answer) - 1:
        if answer[idx - 1] == answer[idx] == '.':
            answer = answer.replace(answer[idx - 1:idx + 1], '.')
            continue
        idx += 1

    # 4단계
    if answer[0:1] == '.':
        answer = answer[1:]
    if answer[len(answer) - 1:] == '.':
        answer = answer[:len(answer) - 1]

    # 5단계
    if len(answer) == 0:
        answer += 'a'

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[len(answer) - 1:] == '.':
        answer = answer[:len(answer) - 1]

    # 7단계
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[len(answer) - 1:]

    return answer

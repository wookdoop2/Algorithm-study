# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/76502
# 월간 코드 챌린지 시즌2
def solution(s):

    length = len(s)
    s = list(s)
    count = 0
    answer = 0

    while count != length:
        stack = []

        # 올바른 괄호 체크
        for string in s:

            if len(stack) == 0:
                stack.append(string)
                continue

            if (stack[-1] == '(' and string == ')') or (stack[-1] == '[' and string == ']') or (stack[-1] == '{' and string == '}'):
                stack.pop()
                continue

            stack.append(string)

        if len(stack) == 0:
            answer += 1

        # 괄호 문자열 회전
        s.append(s.pop(0))
        count += 1

    print(answer)
    # return answer


solution("[](){}")
solution("}]()[{")
solution("}}}")
solution("[)(]")


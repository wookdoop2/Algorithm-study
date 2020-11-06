# Programmers
# level 1
# https://programmers.co.kr/learn/courses/30/lessons/17681
# 2018 KAKAO BLIND RECRUITMENT
def solution(n, arr1, arr2):
    answer = []
    # num = bin(arr1[1])
    # num = list(num)
    for i in range(0, n):
        answer_ = []
        _answer_ = []
        num1 = list(format(arr1[i], 'b'))
        num2 = list(format(arr2[i], 'b'))
        if len(num1) != n:
            for a in range(n - len(num1)):
                num1.insert(a, '0')
        if len(num2) != n:
            for b in range(n - len(num2)):
                num2.insert(b, '0')
        for j in range(0, n):
            answer_.append(int(num1[j]) | int(num2[j]))
        for k in answer_:
            if k == 1:
                _answer_.append('#')
            else:
                _answer_.append(' ')
        answer.append(''.join(_answer_))
    return answer

# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/12941
# 이왜레벨2?
def solution(A, B):
    answer = 0

    A = sorted(A)
    B = sorted(B)

    for i in range(len(A)):
        answer += A[i] * B[len(A) - 1 - i]

    return answer

# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/12980
def solution(n):
    ans = 0

    while True:

        if n == 1:
            ans += 1
            break
        if n == 0:
            break

        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
            n = n // 2
            ans += 1

    return ans

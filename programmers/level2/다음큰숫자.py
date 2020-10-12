# level 2
def count_one(n):
    count = 0
    while 1:
        if n % 2 == 1:
            count += 1
        n = n // 2
        if n == 1:
            return count + 1


def solution(n):
    answer = 0
    num = count_one(n)
    while 1:
        n += 1
        if num == count_one(n):
            return n

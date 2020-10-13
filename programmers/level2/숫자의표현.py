# level 2
def solution(n):
    answer = 1
    for i in range(n - 1, 1, -1):

        if i + (i - 1) > n:
            continue
        else:
            num = 0
            for j in range(i, 0, -1):
                num += j
                if num == n:
                    answer += 1
                    break
                elif num > n:
                    break
    return answer

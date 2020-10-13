# level 2
def solution(citations):
    max_num = max(citations)
    citations.sort(reverse=True)

    if max_num == 0:
        return max_num

    while max_num >= 0:
        num0 = 0
        num1 = 0
        for i in citations:
            if i >= max_num:
                num0 += 1
        for i in citations:
            if max_num >= i:
                num1 += 1
        if num0 >= max_num and num1 <= max_num:
            return max_num
        max_num -= 1

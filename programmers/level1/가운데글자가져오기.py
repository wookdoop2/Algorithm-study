def solution(s):
    answer = ''
    new_list = list(s)
    length = len(new_list)
    if length % 2 == 0:
        answer = new_list[int(length / 2) - 1] + new_list[int(length / 2)]
    else:
        answer = new_list[int(length / 2)]
    return answer

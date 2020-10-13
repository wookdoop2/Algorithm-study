# level 2
# 2020 KAKAO BLIND RECRUITMENT
def compression(s):
    result = []
    num = 1
    for i in range(0, len(s)):
        if i == 0:
            temp = s[i]
            continue
        if s[i] == temp:
            num += 1
        else:
            result.append(str(num))
            num = 1
            result.append(temp)
        temp = s[i]
        if i == len(s) - 1:
            result.append(str(num))
            result.append(temp)
    for i in result:
        if i == '1':
            result.remove(i)
    return result


def solution(s):
    answer = 0
    new_list = []
    new_list_ = []
    length = []
    line = 1
    while True:
        index_sum = 0
        count = 1
        for i in s:
            new_list.append(i)
            if count == line:
                temp = ''.join(new_list)
                new_list_.append(temp)
                count = 1
                new_list = []
                index_sum += 1
                continue
            index_sum += 1
            count += 1
            if index_sum == len(s):
                temp = ''.join(new_list)
                new_list_.append(temp)
                new_list = []
        length.append(len(''.join(compression(new_list_))))
        new_list_ = []
        line += 1
        if line == len(s):
            break
    answer = min(length)
    return answer

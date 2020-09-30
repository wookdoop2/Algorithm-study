def solution(number, k):
    answer = ''
    number = list(number)
    temp = []
    pre_index = 0
    for i in range(0, len(number)):
        if i == 0:
            temp.append(number[i])
        else:
            temp.append(number[i])
            if temp[pre_index] < temp[pre_index + 1]:
                temp.pop(pre_index)
                if len(temp) == 1:
                    continue
            else:
                pre_index += 1
            if len(temp) + len(number[i + 1:]) == len(number) - k:
                # temp.append(number[i + 1:])
                pre_index = i + 1
                break
            if temp[pre_index - 1] < temp[pre_index]:
                temp.pop(pre_index - 1)
                pre_index -= 1
        # print(temp)
    for i in range(pre_index, len(number)):
        temp.append(number[i])
    answer = ''.join(temp)
    return answer

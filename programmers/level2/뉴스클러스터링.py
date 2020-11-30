# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/17677
# 2018 KAKAO BLINK RECRUITMENT
def solution(str1, str2):
    answer = 0
    jakad = 65536

    str1_dict = dict()
    str2_dict = dict()

    for i in range(len(str1) - 1):
        _str_ = str1[i:i + 2].lower()
        if i == 0:
            if _str_.isalpha():
                str1_dict[_str_] = 1
            else:
                continue
        else:
            if _str_.isalpha():
                if _str_ in list(str1_dict.keys()):
                    str1_dict[_str_] += 1
                else:
                    str1_dict[_str_] = 1
            else:
                continue

    for i in range(len(str2) - 1):
        _str_ = str2[i:i + 2].lower()
        if i == 0:
            if _str_.isalpha():
                str2_dict[_str_] = 1
            else:
                continue
        else:
            if _str_.isalpha():
                if _str_ in list(str2_dict.keys()):
                    str2_dict[_str_] += 1
                else:
                    str2_dict[_str_] = 1
            else:
                continue

    # print(str1_dict)
    # print(str2_dict)

    # 공집합 체크
    if len(str1_dict) == 0 and len(str2_dict) == 0:
        return 1 * jakad

    inter = 0
    union = 0

    # Intersection
    for i in str1_dict.keys():
        for j in str2_dict.keys():
            if i == j:
                inter += min(str1_dict[i], str2_dict[j])
                break
    # print(inter)

    # Union
    union_list = list(set(list(str1_dict.keys()) + list(str2_dict.keys())))
    for i in union_list:
        if i in list(str1_dict.keys()) and i in list(str2_dict.keys()):
            union += max(str1_dict[i], str2_dict[i])
        elif i in list(str1_dict.keys()):
            union += str1_dict[i]
        else:
            union += str2_dict[i]
    # print(union)

    answer = int((inter / union) * jakad)

    return answer

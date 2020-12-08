# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/17686
# 2018 KAKAO BLINK RECRUITMENT
def solution(files):
    answer = []
    _list_ = [[0, '', '', ''] for _ in range(len(files))]

    for i in range(len(files)):
        file_name = files[i]
        idx = i
        start_idx = 0
        end_idx = 0

        for j in range(0, len(file_name)):
            if file_name[j].isdigit() == False and file_name[j + 1].isdigit():
                start_idx = j + 1
            elif file_name[j].isdigit() and file_name[j + 1].isdigit() == False:
                end_idx = j + 1
                break
            else:
                continue

        _list_[i][0] = idx
        _list_[i][1] = file_name[:start_idx].lower()
        _list_[i][2] = str(int(file_name[start_idx:end_idx]))
        _list_[i][3] = file_name[end_idx:].lower()
    print(_list_)
    # 정렬
    _list_ = sorted(_list_, key=lambda x: (x[1], x[2], x[3]))

    for i in range(len(_list_)):
        answer.append(files[_list_[i][0]])

    return answer

# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/17686
# 2018 KAKAO BLINK RECRUITMENT
def dividing(idx, name):
    _list_ = ['', '', idx]
    start_idx = 0
    num_length = 0
    num_check = 0

    # Split head, number, tail
    for i in range(len(name)):
        if num_check == 0 and name[i].isdigit():
            num_check = 1
            num_length += 1
            start_idx = i
            continue

        if num_check == 1 and name[i].isdigit():
            num_length += 1

        if num_check == 1 and not name[i].isdigit():
            break

    _list_[0] = name[:start_idx].lower()
    _list_[1] = int(name[start_idx:start_idx + num_length])

    return _list_


def solution(files):
    answer = []
    files_list = []

    for idx, file_name in enumerate(files):
        fn = dividing(idx, file_name)
        files_list.append(fn)

    new_files = sorted(files_list, key=lambda x: (x[0], x[1], x[2]))

    for file in new_files:
        answer.append(files[file[2]])

    return answer

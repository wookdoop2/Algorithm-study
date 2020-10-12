# level 2
def solution(s):
    answer = []
    _list_ = list(map(int, s.split(' ')))
    min_num = 999999
    max_num = 0

    for i in range(len(_list_)):
        if i == 0:
            min_num = _list_[i]
            max_num = _list_[i]
        else:
            if min_num > _list_[i]:
                min_num = _list_[i]
            if max_num < _list_[i]:
                max_num = _list_[i]
    answer.append(min_num)
    answer.append(max_num)
    return ' '.join(map(str, answer))

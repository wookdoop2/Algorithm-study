# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/17683
# 2018 KAKAO BLINK RECRUITMENT
def conversion(_m_):
    _m_ = _m_.replace('C#', 'c')
    _m_ = _m_.replace('D#', 'd')
    _m_ = _m_.replace('F#', 'f')
    _m_ = _m_.replace('G#', 'g')
    _m_ = _m_.replace('A#', 'a')
    return _m_


def cal_music_length(musicinfo_):
    starttime = musicinfo_[0]
    endtime = musicinfo_[1]
    hour = 1 * (int(endtime.split(':')[0]) - int(starttime.split(':')[0]))
    if hour == 0:
        total = int(endtime.split(':')[1]) - int(starttime.split(':')[1])
    else:
        total = 60 * hour + int(endtime.split(':')[1]) - int(starttime.split(':')[1])

    return total


def solution(m, musicinfos):
    answer = dict()
    final_answer = ''

    new_m = conversion(m)

    for i in range(len(musicinfos)):
        _list_ = []
        sheet = ''
        _list_ = musicinfos[i].split(',')
        _list_[3] = conversion(_list_[3])
        # print(_list_)

        music_length = cal_music_length(_list_)
        # print(music_length)

        while len(sheet) <= music_length:
            sheet += _list_[3]
        sheet = sheet[:music_length]

        for i in range(len(sheet)):
            if sheet[i:i + len(new_m)] == new_m:
                answer[_list_[2]] = music_length
                break

    # print(answer)

    keys = list(answer.keys())
    print(keys)
    if len(answer) == 1:
        return keys[0]
    elif len(answer) == 0:
        return "(None)"
    else:
        max_num = 0
        result = ''
        for i in keys:
            l = answer.get(i)
            if max_num < l:
                max_num = l
                result = i
        return result

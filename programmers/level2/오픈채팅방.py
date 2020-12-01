# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/42888
# 2019 KAKAO BLINK RECRUITMENT
def solution(record):

    answer = []
    _dict_ = dict()
    room_logs = []

    for i in range(len(record)):
        msg = list(record[i].split(' '))
        if msg[0] == 'Enter':
            room_logs.append(msg[0] + ' ' + msg[1])
            _dict_[msg[1]] = msg[2]
        elif msg[0] == 'Leave':
            room_logs.append(msg[0] + ' ' + msg[1])
        else:
            _dict_[msg[1]] = msg[2]

    for i in range(len(room_logs)):
        msg = list(room_logs[i].split(' '))
        if msg[0] == 'Enter':
            answer.append(_dict_[msg[1]] + "님이 들어왔습니다.")
        else:
            answer.append(_dict_[msg[1]] + "님이 나갔습니다.")

    # print(answer)

    return answer

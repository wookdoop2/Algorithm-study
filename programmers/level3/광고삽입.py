# Programmers
# level 3
# https://programmers.co.kr/learn/courses/30/lessons/72414
# 2021 KAKAO BLIND RECRUITMENT
def time_to_idx(time):
    time_list = list(map(int, time.split(':')))
    return time_list[0] * 3600 + time_list[1] * 60 + time_list[2]


def idx_to_time(idx):
    hour, minute = divmod(idx, 3600)
    minute, second = divmod(minute, 60)
    return str(hour).zfill(2) + ':' + str(minute).zfill(2) + ':' + str(second).zfill(2)


def solution(play_time, adv_time, logs):

    play_time = list(map(int, play_time.split(':')))
    acc_list = [0] * (play_time[0] * 3600 + play_time[1] * 60
                      + play_time[2] + 1)

    for audience in logs:
        start, end = audience.split('-')
        start = time_to_idx(start)
        end = time_to_idx(end)
        acc_list[start] += 1
        acc_list[end] -= 1

    # 구간별 시청자 수
    for i in range(1, len(acc_list)):
        acc_list[i] = acc_list[i] + acc_list[i - 1]

    adv_idx = time_to_idx(adv_time)

    adv_start = 0
    _sum_ = 0
    max_sum = 0
    for i in range(adv_idx, len(acc_list)):
        _sum_ -= acc_list[i - adv_idx]
        _sum_ += acc_list[i]
        if max_sum < _sum_:
            max_sum = _sum_
            adv_start = i - adv_idx + 1

    return idx_to_time(adv_start)

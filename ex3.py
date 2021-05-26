def solution(ads):
    answer = 0

    ads = sorted(ads, key=lambda x: x[0])

    start_time = dict()
    for start, cost in ads:
        start_time[start] = start_time.get(start, []) + [cost]

    print(start_time)

    start_time_list = list(start_time.keys())
    start = start_time_list[0]
    for i in range(1, len(start_time_list)):

        cost = start_time[start_time_list[i]][0]

        # 시작 시간이 겹칠 때 손해 비용이 작은 광고를 내보낸다

        ads_end_time = start + 5

        next_start = start_time_list[i]

        wait_time = ads_end_time - next_start

        answer += wait_time * cost

        start = ads_end_time

    return answer


solution([[1, 3], [3, 2], [5, 4]])
solution([[5, 2], [2, 2], [6, 3], [9, 2]])
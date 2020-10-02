def solution(a, b):
    answer = ''
    day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    day_num = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_sum = 0

    for i in range(1, a):
        day_sum = day_sum + day_num[i - 1]
    day_sum = day_sum + b

    if day_sum % 7 == 6:
        answer = day[3]
    if day_sum % 7 == 0:
        answer = day[4]
    if day_sum % 7 == 1:
        answer = day[5]
    if day_sum % 7 == 2:
        answer = day[6]
    if day_sum % 7 == 3:
        answer = day[0]
    if day_sum % 7 == 4:
        answer = day[1]
    if day_sum % 7 == 5:
        answer = day[2]

    return answer
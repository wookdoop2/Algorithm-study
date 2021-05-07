# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/49994
# Summmer/Winter Coding(~2018)
def solution(dirs):

    history = set()

    new_y, new_x, y, x = 0, 0, 0, 0

    for direction in dirs:

        if direction == 'U':
            if -5 <= y - 1 <= 5 and -5 <= x <= 5:
                new_y, new_x = y - 1, x
            else:
                continue

        if direction == 'D':
            if -5 <= y + 1 <= 5 and -5 <= x <= 5:
                new_y, new_x = y + 1, x
            else:
                continue

        if direction == 'L':
            if -5 <= y <= 5 and -5 <= x - 1 <= 5:
                new_y, new_x = y, x - 1
            else:
                continue

        if direction == 'R':
            if -5 <= y <= 5 and -5 <= x + 1 <= 5:
                new_y, new_x = y, x + 1
            else:
                continue

        # 중복된 길을 위해 (출발지점, 도착지점) (도착지점, 출발지점)을 set에 모두 넣어준다
        history.add((new_y, new_x, y, x))
        history.add((y, x, new_y, new_x))
        y, x = new_y, new_x

    # 답은 1/2
    print(len(history) // 2)
    # return len(history) // 2


solution("ULURRDLLU")
solution("LULLLLLLU")

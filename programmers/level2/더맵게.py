# Programmers
# level 2
# Heap
# https://programmers.co.kr/learn/courses/30/lessons/42626
def check(scoville, K):
    count = 0
    for i in scoville:
        if i >= K:
            count += 1
    if count == len(scoville):
        return True
    else:
        return False


def solution(scoville, K):
    answer = 0
    total_length = len(scoville)

    while 1:
        front = scoville.pop(0)
        back = scoville.pop(0)
        scoville.insert(0, front + (back * 2))

        answer += 1

        if answer == total_length - 1:
            if scoville[0] < 7:
                return -1
            else:
                return answer

        if check(scoville, K):
            return answer
        else:
            continue

    return answer
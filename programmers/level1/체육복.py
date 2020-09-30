def solution(n, lost, reserve):
    answer = 0
    new_list = list(range(1, n+1))
    lost_ = lost
    reserve_ = reserve
    for i in lost:
        if i in reserve:
            reserve_.remove(i)
            lost_.remove(i)
    print(reserve_)
    print(lost_)
    answer = len(new_list) - len(lost_)
    for i in reserve_:
        new_list = list(range(i-1, i+2))
        for j in lost_:
            if j in new_list:
                lost_.remove(j)
                answer = answer + 1
                break
    return answer

num = int(input())
answer = 0
min_num = [num]


def cal(num_list):
    arr = []
    for _num_ in num_list:
        if _num_ % 3 == 0:
            arr.append(_num_ / 3)
        if _num_ % 2 == 0:
            arr.append(_num_ / 2)
        arr.append(_num_ - 1)
    return arr


while 1:
    if num == 1:
        print(answer)
        break
    tmp = min_num[:]
    min_num = []
    min_num = cal(tmp)
    answer += 1
    if min(min_num) == 1:
        print(answer)
        break

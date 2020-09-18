count, position = input().split()
count = int(count)
position = int(position)

answer = "<"
_list_ = list(range(1, count + 1))

while 1:
    if len(_list_) == 1:
        answer += str(_list_.pop(0)) + ">"
        break
    for i in range(0, position - 1):
        _list_.append(_list_.pop(0))
    answer += str(_list_.pop(0)) + ", "
print(answer)

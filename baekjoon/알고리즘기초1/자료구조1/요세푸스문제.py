count, position = input().split()
count = int(count)
position = int(position)

answer = []
_list_ = list(range(1, count + 1))

for i in range(count - 1):
    for j in range(0, position - 1):
        _list_.append(_list_.pop(0))
    answer.append(_list_.pop(0))
answer.append(_list_.pop(0))
print('<' + ', '.join(map(str, answer)) + '>')

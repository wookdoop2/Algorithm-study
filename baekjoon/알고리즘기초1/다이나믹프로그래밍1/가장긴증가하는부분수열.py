count = int(input())
nums = list(map(int, input().split(' ')))

_list_ = [0] * count

last_num = 0

for i in range(count):
    if i == 0:
        last_num = nums[i]
        _list_[i] = 1
    else:
        if last_num < nums[i]:
            _list_[i] = _list_[i - 1] + 1
            last_num = nums[i]
        else:
            _list_[i] = _list_[i - 1]
            last_num = nums[i]
print(max(_list_))

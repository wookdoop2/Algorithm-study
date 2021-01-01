# Beakjoon Online Judge
# Dynamic Programming
count = int(input())
nums = list(map(int, input().split()))

max_num = 0
_list_ = [0] * count

for i in range(count):
    if i == 0:
        _list_[i] = nums[i]

    if _list_[i - 1] + nums[i] > nums[i]:
        _list_[i] = _list_[i - 1] + nums[i]
    else:
        _list_[i] = nums[i]

print(max(_list_))

# Beakjoon Online Judge
# Dynamic Programming
count = int(input())
nums = list(map(int, input().split()))

_list_ = [0] * count

_list_[0] = 1

for i in range(1, count):
    _list_[i] = 1
    for j in range(0, i):
        if nums[j] < nums[i] and _list_[j] + 1 > _list_[i]:
            _list_[i] = _list_[j] + 1

print(max(_list_))

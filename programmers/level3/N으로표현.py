# level 3
# Dynamic Programming
def solution(N, number):
    _set_ = [set() for i in range(9)]
    _set_[0].add(0)
    _set_[1].add(N)
    for i in range(2, 9):
        _set_[i].add(int(str(N) * i))
        for j in range(1, i):
            for k in _set_[j]:
                _set_[i].add(int(k + N))
                _set_[i].add(int(k - N))
                _set_[i].add(int(k * N))
                _set_[i].add(int(k / N))
        if number in _set_[i]:
            return i
    return -1


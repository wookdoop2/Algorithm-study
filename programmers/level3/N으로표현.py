# level 3
# Dynamic Programming
def solution(N, number):
    _set_ = [set() for i in range(9)]
    _set_[0].add(0)
    for i in range(1, 9):
        _set_[i].add(int(str(N) * i))
        for j in range(1, i):
            for k in _set_[j]:
                for m in _set_[i - j]:
                    _set_[i].add(k + m)
                    _set_[i].add(k - m)
                    _set_[i].add(k * m)
                    if m != 0:
                        _set_[i].add(k // m)
        if number in _set_[i]:
            return i
    return -1

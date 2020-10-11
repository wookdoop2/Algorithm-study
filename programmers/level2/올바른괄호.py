def solution(s):
    _list_ = []
    for i in range(len(s)):
        if s[i] == ')':
            if len(_list_) == 0:
                _list_.append(s[i])
            else:
                _list_.pop()
        else:
            _list_.append(s[i])

    if len(_list_) == 0:
        return True
    else:
        return False

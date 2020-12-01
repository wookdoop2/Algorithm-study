# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/17680
# 2018 KAKAO BLINK RECRUITMENT
def solution(cacheSize, cities):
    answer = 0

    if cacheSize == 0:
        return len(cities) * 5

    _list_ = [0] * cacheSize
    _cache_ = [0] * cacheSize

    for i in range(len(cities)):
        idx = i % cacheSize
        city = cities[i].lower()

        # Time passes when put it
        for j in range(len(_list_)):
            _list_[j] += 1

        if city in _cache_:  # cache hit
            _list_[_cache_.index(city)] = 0
            answer += 1

        else:  # cache miss

            max_num = 0
            for k in range(len(_list_)):
                if _list_[k] > max_num:
                    max_num = _list_[k]

            max_idx = _list_.index(max_num)
            _cache_[max_idx] = city
            _list_[max_idx] = 0
            answer += 5

        # print(_cache_)
        # print(_list_)
        # print()

    return answer

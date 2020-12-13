# Baekjoon Online Judge
# Simulation
# https://www.acmicpc.net/problem/1924
date = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month, day = map(int, input().split())

_time_ = 0
for idx in range(month - 1):
    _time_ += days[idx]

_time_ = _time_ + day
print(date[_time_ % 7])

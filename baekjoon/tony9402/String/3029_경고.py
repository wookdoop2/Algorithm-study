# Baekjoon Online Judge
# String
# https://www.acmicpc.net/problem/3029
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

present = list(map(int, input().rstrip().split(':')))
throwing_time = list(map(int, input().rstrip().split(':')))

# hh:mm:ss를 초 단위로 변환
present_time_to_sec = present[0] * 60 * 60 + present[1] * 60 + present[2]
throwing_time_to_sec = throwing_time[0] * 60 * 60 + throwing_time[1] * 60 + throwing_time[2]

new_time = 0
final_h = 0
final_m = 0
final_s = 0

# print(present)

# 같은 시간대면 24시간 기다리기
if present_time_to_sec == throwing_time_to_sec:
    print("24:00:00")
    exit()

if present_time_to_sec < throwing_time_to_sec:
    new_time = throwing_time_to_sec - present_time_to_sec

# 현재 시간이 더 크면 = 24시 - 현재 시간 + 폭발 시간
if present_time_to_sec > throwing_time_to_sec:
    new_time = 24 * 60 * 60 - present_time_to_sec + throwing_time_to_sec

# 초 단위를 hh:mm:ss로 변환
final_h = new_time // 60 // 60
final_m = new_time // 60 % 60
final_s = new_time % 60

print(str(final_h).zfill(2) + ':' + str(final_m).zfill(2) + ':' + str(final_s).zfill(2))

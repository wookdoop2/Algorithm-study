# Baekjoon Online Judge
# Brute Force
# https://www.acmicpc.net/problem/1107
# 2020 NHN godo 하반기 공채
buttons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
not_broken = []

page = int(input())
count = int(input())
if count == 0:
    not_broken = buttons
else:
    broken = list(map(int, input().split()))

    # Not broken buttons
    for i in buttons:
        if i not in broken:
            not_broken.append(i)

max_page = 500000

answer = abs(page - 100)

# 0 ~ 1000000
for i in range(0, (max_page * 2) + 1):
    num = str(i)
    for j in range(len(num)):
        if int(num[j]) not in not_broken:
            break
        elif j == len(num) - 1:
            answer = min(answer, len(num) + abs(page - i))

print(answer)

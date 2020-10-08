count = int(input())
sequence = list(map(int, input().split()))

# 시간초과
# answer = []
# _answer_ = []
# for i in range(0, count):
#     for j in range(i + 1, count):
#         if sequence[j] > sequence[i]:
#             break
#     if len(_answer_) == 0:
#         answer.append(-1)
#     else:
#         answer.append(_answer_[0])
#     _answer_ = []
#
# print(' '.join(map(str, answer)))

answer = [0] * count
s = [0]
for i in range(1, count):
    if not s:
        s.append(i)
    while s and sequence[s[-1]] < sequence[i]:
        answer[s.pop()] = sequence[i]
    s.append(i)

while s:
    answer[s.pop()] = -1
print(' '.join(map(str, answer)))

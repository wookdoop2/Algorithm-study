count = int(input())
sequence = list(map(int, input().split()))

answer = [0] * count
index = [0]

frequent = [0] * 10000001
for i in range(0, count):
    frequent[sequence[i]] += 1

for i in range(1, count):
    if not index:
        index.append(i)
    while index and frequent[sequence[index[-1]]] < frequent[sequence[i]]:
        answer[index.pop()] = sequence[i]
    index.append(i)

while index:
    answer[index.pop()] = -1
print(' '.join(map(str, answer)))

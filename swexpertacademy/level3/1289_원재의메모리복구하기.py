# SW Expert Academy
# Difficulty 3

T = int(input())

for test_case in range(1, T + 1):
    memory = list(map(int, input()))
    original = [0] * len(memory)

    answer = 0

    for i in range(len(memory)):
        if memory[i] != original[i]:
            for j in range(i, len(memory)):
                original[j] = memory[i]
            answer += 1

    print("#{} {}".format(test_case, answer))

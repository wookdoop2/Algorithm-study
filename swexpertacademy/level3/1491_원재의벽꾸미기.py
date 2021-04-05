# SW Expert Academy
# Difficulty 3

T = int(input())

for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())

    answer = -1

    for i in range(1, N + 1):
        j = 1
        while True:
            if i * j > N:
                break
            num = A * abs(i - j) + B * (N - (i * j))
            if answer == -1:
                answer = num
            else:
                answer = min(answer, num)
            j += 1

    print("#{} {}".format(test_case, answer))

# while문과 for문의 차이?

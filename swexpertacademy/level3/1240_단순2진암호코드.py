# SW Expert Academy
# Difficulty 3

code_list = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4', '0110001': '5', '0101111': '6',
             '0111011': '7', '0110111': '8', '0001011': '9'}


def CODE():
    for y in range(N):
        for x in range(M - 1, -1, -1):
            if input_code[y][x] == '1':
                return input_code[y][x - 55:x + 1]


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    input_code = [input() for _ in range(N)]

    _code_ = CODE()

    final_code = ''
    for i in range(0, len(_code_) - 6, 7):
        final_code += code_list[''.join(_code_[i:i+7])]

    # print(final_code)

    even_sum = 0
    odd_sum = 0
    identity_code = int(final_code[-1])

    for idx in range(len(final_code) - 1):
        if idx % 2 == 0:
            odd_sum += int(final_code[idx])
        else:
            even_sum += int(final_code[idx])

    # print(even_sum)
    # print(odd_sum)
    # print(identity_code)

    if (odd_sum * 3 + even_sum + identity_code) % 10 == 0:
        print("#{} {}".format(test_case, sum(map(int, final_code))))
    else:
        print("#{} {}".format(test_case, 0))

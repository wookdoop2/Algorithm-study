# SW Expert Academy
# Difficulty 3

T = int(input())

for test_case in range(1, T + 1):

    P = input().rstrip()
    Q = input().rstrip()

    if P + 'a' == Q:
        result = 'N'
    else:
        result = 'Y'

    print(f'#{test_case} {result}')

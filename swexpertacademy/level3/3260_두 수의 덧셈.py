# SW Expert Academy
# Difficulty 3

T = int(input())

for test_case in range(T):
    A, B = map(int, input().split())

    print("#{} {}".format(test_case + 1, A + B))

# SW Expert Academy
# Difficulty 3

role = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

T = int(input())

for _ in range(1, T + 1):
    test_case, length = map(str, input().split())
    num_list = list(input().split())

    new_num_list = []
    for s in num_list:
        new_num_list.append([s, role[s]])   # [문자열, 문자열 해당 숫자] 형식으로 저장

    # 문자열 해당 숫자를 기준으로 정렬
    c = sorted(new_num_list, key=lambda x: x[1])

    print(test_case)
    for s in c:
        print(s[0], end=' ')

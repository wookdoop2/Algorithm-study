# SW Expert Academy
# Difficulty 3


def dfs(count):

    global answer
    global card_list

    # 교환 횟수 소진
    if count == 0:
        temp = int(''.join(card_list))
        if temp > answer:
            answer = temp
        return

    for i in range(len(card_list) - 1):
        for j in range(i + 1, len(card_list)):

            card_list[i], card_list[j] = card_list[j], card_list[i]

            # dfs 연산 시간을 줄이기 위해 숫자판 정보 딕셔너리에 저장
            if (''.join(card_list), count - 1) not in cards_dict.keys():
                cards_dict[(''.join(card_list), count - 1)] = 1
                dfs(count - 1)
            card_list[i], card_list[j] = card_list[j], card_list[i]


T = int(input())

for test_case in range(1, T + 1):
    cards, count = input().split(' ')
    card_list = list(cards)
    count = int(count)

    answer = 0
    cards_dict = {}

    dfs(count)

    # print(cards_dict)
    print("#{} {}".format(test_case, answer))

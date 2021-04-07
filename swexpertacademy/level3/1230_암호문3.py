# SW Expert Academy
# Difficulty 3

for test_case in range(1, 11):
    N1 = int(input())
    code = list(map(int, input().split()))
    N2 = int(input())
    order_list = list(input().split())

    for i in range(len(order_list)):

        if order_list[i] == 'I':
            for j in range(int(order_list[i + 2])):
                code.insert(int(order_list[i + 1]) + j, int(order_list[i + 3 + j]))

        if order_list[i] == 'D':
            for j in range(int(order_list[i + 2])):
                code.remove(code[int(order_list[i + 1])])

        if order_list[i] == 'A':
            for j in range(int(order_list[i + 1])):
                code.append(int(order_list[i + 2 + j]))

    print("#{}".format(test_case), end=' ')
    for i in range(10):
        print(code[i], end=' ')
    print()

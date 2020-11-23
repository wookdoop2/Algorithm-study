# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/67257
# 2020 카카오 인턴십
from itertools import permutations


def operatoring(expression):
    operators = set()
    _expression_ = []
    num = ''

    for i in expression:
        if i == '+' or i == '-' or i == '*':
            operators.add(i)
            _expression_.append(int(num))
            _expression_.append(i)
            num = ''
        else:
            num += i

    _expression_.append(int(num))
    operators = list(operators)

    _operators_ = permutations(operators, len(operators))

    return list(_operators_), _expression_


def operation(num0, num1, op):
    if op == '+':
        return num0 + num1
    elif op == '-':
        return num0 - num1
    else:
        return num0 * num1


def solution(expression):
    answer = 0

    _operator_, _list_ = operatoring(expression)

    for i in _operator_:
        tmp_list = _list_
        for j in list(i):
            idx = 0
            tmp = []
            while True:
                if tmp_list[idx] == j:
                    tmp.append(operation(tmp.pop(len(tmp) - 1), tmp_list[idx + 1], j))
                    idx += 2
                else:
                    tmp.append(tmp_list[idx])
                    idx += 1

                if idx == len(tmp_list):
                    break

            tmp_list = tmp

        answer = max(answer, abs(tmp_list[0]))

    return answer

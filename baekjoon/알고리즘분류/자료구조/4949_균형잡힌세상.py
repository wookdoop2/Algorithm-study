# Baekjoon Online Judge
# Data Structure
# https://www.acmicpc.net/problem/4949

import sys

input = sys.stdin.readline

# 괄호 문자열 확인용 list
real_string = ['(', ')', '[', ']']

while True:

    string_list = list(input().rstrip())

    # 입력의 종료조건
    if len(string_list) == 1:
        exit()

    _list_ = []
    # print(string_list)

    for s in string_list:
        if s in real_string:  # 괄호 문자열만 체크

            # 맨처음에는 무조건 넣어주기
            if len(_list_) == 0:
                _list_.append(s)
                continue

            # 균형을 이룰 때, 닫히는 괄호를 push하지 않고 열리는 괄호를 pop 해준다.
            if (_list_[-1] == '(' and s == ')') or (_list_[-1] == '[' and s == ']'):
                _list_.pop()
            else:
                _list_.append(s)

    if len(_list_) == 0:
        print("yes")
    else:
        print("no")

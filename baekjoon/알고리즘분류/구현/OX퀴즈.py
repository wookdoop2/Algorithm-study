# Baekjoon Online Judge
# Simulation
# https://www.acmicpc.net/problem/1107
count = int(input())

for i in range(count):
    quiz = input()
    _list_ = []
    answer = 0
    for j in range(len(quiz)):
        if quiz[j] == 'O':
            _list_.append('O')
            answer += len(_list_)
        else:
            _list_ = []
    print(answer)

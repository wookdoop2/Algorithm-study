# Programmers
# level 2
# DFS
# https://programmers.co.kr/learn/courses/30/lessons/43165
def solution(numbers, target):
    answer = 0
    super_node = [0]
    for i in numbers:
        node = []
        for j in super_node:
            node.append(j + i)
            node.append(j - i)
        super_node = node
    answer = super_node.count(target)
    return answer

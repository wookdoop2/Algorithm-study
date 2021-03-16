# Programmers
# level 3
# https://programmers.co.kr/learn/courses/30/lessons/43163
# 깊이/너비 우선 탐색(DFS/BFS)
from collections import deque


def check(word, target):    # 한 개의 알파벳만 바꿔 만들 수 있는 단어 체크
    count = 0

    for i in range(len(word)):
        if word[i] == target[i]:
            count += 1

    if count == len(word) - 1:
        return True
    else:
        return False


def bfs(begin, target, words, visited):

    _list_ = deque()
    _list_.append([begin, 0])   # begin 단어와 단계 수 초기화

    while _list_:

        _word_, count = _list_.popleft()

        if _word_ == target:    # popleft한 단어가 target 단어와 같으면 단계 return
            return count

        for i in range(len(words)):
            if visited[i] != 1 and check(_word_, words[i]):
                _list_.append([words[i], count + 1])
                visited[i] = 1


def solution(begin, target, words):

    if target not in words: # words 배열에 target 단어 없으면 target 단어를 만들 수 없음
        return 0

    visited = [0] * len(words)

    # print(dfs(begin, target, words, visited))

    return bfs(begin, target, words, visited)


solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])

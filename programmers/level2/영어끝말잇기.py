# Programmers
# level 2
# Stack
# https://programmers.co.kr/learn/courses/30/lessons/12981
def solution(n, words):
    answer = []
    word_history = []
    person = 0
    phase = 0

    for i in range(len(words)):
        # first person with first word
        if i == 0:
            word_history.append(words[i])
            person += 1
            continue

        # count phase
        if len(word_history) % n == 0:
            phase += 1

        # repeated person
        person %= n

        # check false case (already used | not match last word and first word
        if (words[i] in word_history) | (word_history[-1][-1] != words[i][0]):
            answer.append(person + 1)
            answer.append(phase + 1)
            return answer

        person += 1
        word_history.append(words[i])

    return [0, 0]

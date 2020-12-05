# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/17684
# 2018 KAKAO BLINK RECRUITMENT
def solution(msg):
    answer = []
    dictionary = dict()

    # Create a dictionary
    for i in range(26):
        dictionary[chr(ord('A') + i)] = i + 1

    while True:

        word_list = list(dictionary.keys())
        num_list = list(dictionary.values())
        idx = 0
        strings = ''

        # Detect words in dictionary
        for i in range(len(msg), 0, -1):
            idx = i
            strings = msg[:idx]
            if strings in word_list:
                break

        answer.append(dictionary[strings])

        # Remove w from input
        msg = msg[idx:]

        # Add word to dictionary
        if len(msg) != 0:
            dictionary[strings + msg[:1]] = len(num_list) + 1
        else:
            return answer

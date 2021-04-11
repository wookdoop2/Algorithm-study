# SW Expert Academy
# Difficulty 3


def rotate_key(key, length):
    _list_ = [[] for _ in range(length)]

    for i in range(length):
        for j in range(length):
            _list_[j].insert(0, key[i][j])

    return _list_


def check(word):
    for i in range(len(word) // 2):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True


for test_case in range(1, 11):
    word_length = int(input())  # 회문 길이
    board_len = 8  # 글자판 길이

    board0 = [list(input()) for _ in range(board_len)]  # 가로
    board1 = rotate_key(board0, board_len)  # 세로 -> 가로

    answer = 0

    # 글자판 순회
    for i in range(board_len):
        for j in range(0, board_len - word_length + 1):

            words0 = board0[i][j:j + word_length]
            words1 = board1[i][j:j + word_length]

            if check(words0):  # 회문인지 아닌지 확인
                answer += 1
            if check(words1):
                answer += 1

    print("#{} {}".format(test_case, answer))

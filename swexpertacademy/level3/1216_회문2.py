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
    N = int(input())
    board0 = [list(input()) for _ in range(100)]
    board1 = rotate_key(board0, 100)

    answer = 1

    for word_length in range(100, 0, -1):  # 회문 길이 100 ~ 1

        for i in range(100):
            for j in range(0, 100 - word_length + 1):

                words0 = board0[i][j:j + word_length]
                words1 = board1[i][j:j + word_length]

                if check(words0) or check(words1):  # 회문인지 아닌지 확인
                    if word_length > answer:
                        answer = word_length
                        break

    print("#{} {}".format(test_case, answer))

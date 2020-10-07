def solution(strings, n):
    strings = sorted(strings)
    answer = sorted(strings, key=lambda element: element[n])
    # answer = []
    # list_ = []
    # temp = []
    # for i in range(len(strings)):
    #     list_.append(list(strings[i]))
    # print(list_)
    # i = 0
    # while(True):
    #     if list_[i][n] > list_[i+1][n]:
    #         temp = list_[i][n]
    #         list_[i][n] = list_[i+1][n]
    #         list_[i+1][n] = temp
    #     i = i + 1
    # print(list_)
    return answer

# 2019 카카오 개발자 겨울 인턴십
def solution(board, moves):
    answer = 0
    length = len(board)
    index = 0
    new_list = []
    for m in moves:
        for i in range(0, length):
            if board[i][m - 1] != 0:
                new_list.append(board[i][m - 1])
                board[i][m - 1] = 0
                break
        if len(new_list) == 0 or len(new_list) == 1:
            continue
        else:
            if new_list[-1] == new_list[-2]:
                new_list.pop(-1)
                new_list.pop(-1)
                answer += 2
    return answer

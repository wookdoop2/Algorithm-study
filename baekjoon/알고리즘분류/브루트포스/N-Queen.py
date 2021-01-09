# Baekjoon Online Judge
# Brute Force | Back Tracking
# https://www.acmicpc.net/problem/9663
def n_queen(_list_, N):
    global count

    if len(_list_) == N:
        count += 1
        return 0

    candidate_list = list(range(N))     # 다음 행 후보자 위치

    for i in range(len(_list_)):
        if _list_[i] in candidate_list:     # 같은 열 체크
            candidate_list.remove(_list_[i])

        if _list_[i] + (len(_list_) - i) in candidate_list:     # 오른쪽 대각선 체크
            candidate_list.remove(_list_[i] + (len(_list_) - i))

        if _list_[i] - (len(_list_) - i) in candidate_list:     # 왼쪽 대각선 체크
            candidate_list.remove(_list_[i] - (len(_list_) - i))

    if len(candidate_list) != 0:
        for i in candidate_list:
            _list_.append(i)
            n_queen(_list_, N)
            _list_.pop()
    else:
        return 0


N = int(input())

count = 0
for i in range(N):      # 최상단 행 시작
    n_queen([i], N)
print(count)

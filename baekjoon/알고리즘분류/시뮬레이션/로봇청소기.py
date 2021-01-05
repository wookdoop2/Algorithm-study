# Baekjoon Online Judge
# Simulation
# https://www.acmicpc.net/problem/14503

def clean(x, y, d):

    global answer

    # 현재 위치 체크
    if _list_[x][y] == 0:
        _list_[x][y] = 2
        answer += 1

    # 4방향 체크
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if _list_[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd

    # 뒷 방향 체크
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]

    # 뒤에도 벽일 때
    if _list_[nx][ny] == 1:
        return

    # 뒤에 빈칸이 있을 때
    clean(nx, ny, d)


N, M = map(int, input().split())
r, c, d = map(int, input().split())
_list_ = []
for i in range(N):
    _list_.append(list(map(int, input().split())))
# print(_list_)

# 북 = 0, 동 = 1, 남 = 2, 서 = 3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0
clean(r, c, d)
print(answer)

# Reference - https://chldkato.tistory.com/157

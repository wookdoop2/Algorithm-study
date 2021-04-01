# SW Expert Academy
# Difficulty 3


def dfs(start_node, ans):

    global answer

    # 탐색한 노드는 체크하고
    visited[start_node] = 1

    ans += 1

    if answer < ans:
        answer = ans

    for adjacent in _list_[start_node]:
        if visited[adjacent] != 1:
            dfs(adjacent, ans)

    # 사용 해제
    visited[start_node] = 0


T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())

    _list_ = [[] for _ in range(N + 1)]

    if M == 0:
        print("#{} {}".format(test_case + 1, 1))
    else:

        answer = 0

        for i in range(M):
            x, y = map(int, input().split())
            _list_[x].append(y)
            _list_[y].append(x)

        # print(_list_)
        visited = [0] * (N + 1)

        for s_node in range(1, N + 1):
            dfs(s_node, 0)

        print("#{} {}".format(test_case + 1, answer))

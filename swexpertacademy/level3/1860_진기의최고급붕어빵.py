def solution(n, m, k, _list_):
    _list_.sort()
    count = 0   # 왔다 간 손님 수

    for t in _list_:
        bread = (t // m) * k    # 손님이 온 시간 기준 남아있는 빵의 갯수
        if bread - count <= 0:
            return 0
        else:
            count += 1

    return 1


T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    person_list = list(map(int, input().split()))
    flag = solution(N, M, K, person_list)

    if flag == 0:
        print("#{} {}".format(test_case, "Impossible"))
    else:
        print("#{} {}".format(test_case, "Possible"))

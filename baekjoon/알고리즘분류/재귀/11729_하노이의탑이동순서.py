# Baekjoon Online Judge
# Recursion
# https://www.acmicpc.net/problem/11729


def hanoi(start, end, size):

    if size == 1:
        route.append([start, end])
        return

    hanoi(start, 6 - start - end, size - 1)
    route.append([start, end])
    hanoi(6 - start - end, end, size - 1)


N = int(input())

route = []
hanoi(1, 3, N)

print(len(route))
for s, e in route:
    print("{} {}".format(s, e))

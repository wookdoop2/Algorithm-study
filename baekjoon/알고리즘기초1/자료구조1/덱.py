from collections import deque
import sys

count = int(sys.stdin.readline())

dq = deque()


def empty():
    if len(dq) == 0:
        return 1
    else:
        return 0


for i in range(count):
    msg = list(sys.stdin.readline().split())
    if msg[0] == "push_back":
        dq.append(msg[1])
    elif msg[0] == "push_front":
        dq.appendleft(msg[1])
    elif msg[0] == "pop_back":
        if empty() == 1:
            print("-1")
        else:
            print(dq.pop())
    elif msg[0] == "pop_front":
        if empty() == 1:
            print("-1")
        else:
            print(dq.popleft())
    elif msg[0] == "back":
        if empty() == 1:
            print(-1)
        else:
            print(dq[len(dq) - 1])
    elif msg[0] == "front":
        if empty() == 1:
            print("-1")
        else:
            print(dq[0])
    elif msg[0] == "size":
        print(len(dq))
    elif msg[0] == "empty":
        print(empty())

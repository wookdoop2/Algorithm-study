from collections import deque

count = int(input())

dq = deque()

for i in range(count):
    msg = list(input().split())
    if msg[0] == "push_back":
        dq.appendleft(msg[1])
    elif msg[0] == "push_front":
        dq.append(msg[1])
    elif msg[0] == "pop_back":
        dq.popleft()
    elif msg[0] == "pop_front":
        dq.pop()
    elif msg[0] == "back":
        print(dq[0])
    elif msg[0] == "front":
        print(dq[len(dq) - 1])
    elif msg[0] == "size":
        print(len(dq))
    elif msg[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)

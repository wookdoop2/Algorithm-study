msg = input()

check = 0
answer = []
_msg_ = []

for i in range(0, len(msg)):
    if msg[i] == '<':
        answer += _msg_
        answer.append(msg[i])
        check = 1
        _msg_ = []
    elif msg[i] == ' ':
        answer += _msg_
        answer.append(msg[i])
        _msg_ = []
    elif msg[i] == '>':
        answer.append(msg[i])
        check = 0
    elif check == 1:
        answer.append(msg[i])
    else:
        _msg_.insert(0, msg[i])
answer += _msg_
print(''.join(answer))







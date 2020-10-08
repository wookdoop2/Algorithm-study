stick = input()

stack = []
count = 0
index = 0

while index <= len(stick) - 2:
    if stick[index] == '(' and stick[index + 1] == ')':
        count += len(stack)
        index += 2
        continue
    if stick[index] == '(':
        stack.append(stick[index])
    if stick[index] == ')':
        stack.pop()
        count += 1
    index += 1
count += 1

print(count)

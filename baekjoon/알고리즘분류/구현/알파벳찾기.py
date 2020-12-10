# Baekjoon Online Judge
# Simulation
# https://www.acmicpc.net/problem/10809
words = list(input())

alpha_list = []
for i in range(0, 26):
    alpha_list.append(chr(ord('a') + i))

for i in range(len(alpha_list)):
    check = 0
    for j in range(len(words)):
        if words[j] == alpha_list[i]:
            alpha_list[i] = str(j)
            check = 1
            break

    if check == 0:
        alpha_list[i] = str(-1)
    else:
        continue

print(' '.join(alpha_list))

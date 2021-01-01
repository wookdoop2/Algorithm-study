# Baekjoon Online Judge
# Simulation
# https://www.acmicpc.net/problem/1157
word = list(input().upper())

spell_set = set(word)

count_list = []
for i in spell_set:
    count_list.append(word.count(i))

# print(set(word))
# print(count_list)

if count_list.count(max(count_list)) > 1:
    print('?')
else:
    max_index = count_list.index(max(count_list))
    print(list(spell_set)[max_index])

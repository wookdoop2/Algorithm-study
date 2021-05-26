# Baekjoon Online Judge
# Trie
# https://www.acmicpc.net/problem/4358
# 출처 : https://github.com/tony9402/baekjoon

import sys

input = sys.stdin.readline

tree_dict = dict()
total_tree_num = 0

while True:

    tree = input().rstrip()

    if tree == '':
        break

    if tree in tree_dict.keys():
        tree_dict[tree] += 1
    else:
        tree_dict[tree] = 1

    total_tree_num += 1

tree_list = list(tree_dict.keys())
tree_list.sort()
for t in tree_list:
    print("{} {:.4f}".format(t, (tree_dict[t] / total_tree_num) * 100))

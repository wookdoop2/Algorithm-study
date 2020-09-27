def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        index = 0
        check = 1
        new_list = []
        for j in i:
            if j not in skill:
                continue
            if index < skill.index(j):
                check = 0
                break
            else:
                index += 1
        if check == 1:
            answer += 1
    return answer

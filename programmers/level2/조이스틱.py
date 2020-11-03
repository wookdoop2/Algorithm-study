# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/42860
def solution(name):
    answer = 0
    name = list(name)
    # for i in name:
    #     print(ord(i) - ord('A'), ord('Z') - ord(i) + 1)
    # print(9 + (1 + 4) + (1 + 9) + (1 + 12) + (1 + 4) + (1 + 13))
    index_list = list(range(0, len(name)))
    location = ord('A')
    index = 0
    count = 0
    while True:
        print(index_list)
        mov_min = []
        if count == 0:
            answer += ord(name[index]) - location
            index_list.pop(index)
        else:
            for i in index_list:
                a = ord('Z') - ord(name[i]) + 1
                b = ord(name[i]) - ord('A')
                if a > b:
                    mov_min.append(b)
                else:
                    mov_min.append(a)
            for i in range(0, len(mov_min)):
                if i == len(mov_min) - 1:
                    mov_min[i] += 1
                elif mov_min[i] == 0:
                    continue
                else:
                    mov_min[i] += (i + 1)
            print(mov_min)
            index_left = 0
            index_right = len(mov_min) - 1
            for i in range(0, len(mov_min)):
                if mov_min[index_right] == 0:
                    index_right += 1
                else:
                    break
                if mov_min[index_left] == 0:
                    index_right += 1
                else:
                    break
            temp = min(mov_min[index_right], mov_min[index_left])
            answer += temp
            index = mov_min.index(temp) + 1
            index_list.pop(index - 1)
        count += 1
        if len(index_list) == 0:
                break
    print(answer)
    return answer
# Programmers
# level 2
# https://programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = []
    # counting = [0 for i in range(truck_weights)]
    weight_ = 0
    index = 0
    # while True:
    #     for i in truck_weights:
    #         on_bridge.append(i)
    #         if sum(on_bridge) > weight:
    #             on_bridge.pop(len(on_bridge) - 1)
    #     mylist = [0 for i in range(len(on_bridge))]
    # while True:
    #     for i in truck_weights:
    #         if sum(on_bridge) < weight:
    #             on_bridge.append(truck_weights[index])
    #     for i in truck_weights:
    #         if i in on_bridge:
    #             counting[i]
    #     answer += 1
    for i in truck_weights:
        count = 0
        while True:
            if sum(on_bridge) < weight:
                on_bridge.append(i)
            count += 1
            if count == bridge_length:
                on_bridge.pop(0)
                break
            answer += 1
    answer = answer + len(truck_weights)
    return answer

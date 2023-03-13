from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque()
    bridge_weight = 0

    while truck_weights or bridge:
        answer += 1
        if bridge:
            temp = bridge.popleft()
            bridge_weight -= temp[0]
            if temp[1] + bridge_length != answer:
                bridge.appendleft(temp)
                bridge_weight += temp[0]

        if truck_weights:
            truck = truck_weights.popleft()
            if bridge_weight + truck <= weight:
                bridge.append((truck, answer))
                bridge_weight += truck
            else:
                truck_weights.appendleft(truck)

    return answer
a = 2
b = 10
c = [7,4,5,6]
print(solution(a,b,c))
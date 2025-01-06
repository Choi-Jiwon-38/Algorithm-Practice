from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    truck_q = deque(truck_weights)
    bridge_q = deque([0 for _ in range(bridge_length)])
    
    curr_weight = 0
    
    while len(truck_q):
        answer += 1
        pop_item = bridge_q.popleft()
        curr_weight -= pop_item
        
        if curr_weight + truck_q[0] <= weight:
            pop_truck = truck_q.popleft()
            bridge_q.append(pop_truck)
            curr_weight += pop_truck
        else:
            bridge_q.append(0)
        
    return answer + bridge_length
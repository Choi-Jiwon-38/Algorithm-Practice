from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([])
    trucks = deque(truck_weights)
    rest = weight
    time = 0
    
    while (trucks):
        time += 1

        
        while bridge and bridge[0][1] <= time:
            passed_weight, _ = bridge.popleft()
            rest += passed_weight
        
    
        if rest >= trucks[0]:
            truck = trucks.popleft()
            bridge.append([truck, time + bridge_length])
            rest -= truck
        else:
            passed_weight, a_time = bridge.popleft()
            time = a_time
            rest += passed_weight

            if rest >= trucks[0]:
                truck = trucks.popleft()
                bridge.append([truck, time + bridge_length])
                rest -= truck
                
    if bridge:
        return bridge[-1][1]
        
    return time
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 1
    bridge = deque([])
    trucks = deque(truck_weights)    
    rest = weight
    
    while trucks:
        # 다리 다 건넌 경우에는 내림
        if bridge and bridge[0][1] <= time:
            rest += bridge[0][0]
            bridge.popleft()
        
        if rest >= trucks[0]:
            bridge.append([trucks[0], time + bridge_length])
            rest -= trucks[0]
            trucks.popleft()
            time += 1

        elif bridge:
            time = bridge[0][1]
            
    if bridge:
        return bridge[-1][1]

    return time

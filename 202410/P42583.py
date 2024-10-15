from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = deque([[truck_weights[i], 0] for i in range(len(truck_weights))])
    
    cnt = 0
    bridge_weight = 0
    bridge = deque([])
    while trucks:
        if len(bridge) > 0:
            if bridge[0][1] == bridge_length:
                bridge_weight -= bridge[0][0]
                bridge.popleft()
                
        if bridge_weight+trucks[0][0] <= weight:
            bridge_weight += trucks[0][0]
            now = trucks.popleft()
            bridge.append(now)
            
        for truck in bridge:
            truck[1] +=1
        cnt += 1
            
    return cnt + bridge_length
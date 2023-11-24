from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([])
    how_go = deque([])
    start = deque(truck_weights)
    sec = 1

    while bridge or start :
        if not bridge and start:
            bridge.append(start.popleft())
            how_go.append(1)
        else :
            for i in range(len(how_go)) :
                    how_go[i] += 1
            if start :
                if sum(bridge) + start[0] <= weight :
                    bridge.append(start.popleft())
                    how_go.append(1)
        
        if how_go[0] == bridge_length :
             bridge.popleft()
             how_go.popleft()
        
        sec += 1

    return sec

# bridge_length = 2
# weight = 10
# truck_weights = [7,4,5,6]

# bridge_length = 100
# weight = 100
# truck_weights = [10]

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

solution(bridge_length, weight, truck_weights)
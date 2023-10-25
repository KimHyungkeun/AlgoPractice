import sys
from collections import deque

n, w, l = map(int, sys.stdin.readline().split())
trucks = deque(list(map(int, sys.stdin.readline().split())))
trucks_distance = deque([])
bridge = deque([])

sec = 1
while bridge or trucks :
    if not bridge and trucks :
        bridge.append(trucks.popleft())
        trucks_distance.append(1)
    elif bridge and trucks :
        if sum(bridge) + trucks[0] > l :
            for i in range(len(trucks_distance)) :
                trucks_distance[i] += 1 
        else :
            for i in range(len(trucks_distance)) :
                trucks_distance[i] += 1 
            bridge.append(trucks.popleft())
            trucks_distance.append(1)
    else :
        for i in range(len(trucks_distance)) :
            trucks_distance[i] += 1 
    
    if trucks_distance[0] == w :
        bridge.popleft()
        trucks_distance.popleft()
    
    sec += 1
    

print(sec)

     

def solution(order):
    answer = 0
    truck = []
    base_belt = sorted(order, reverse=True)
    sub_belt = []
    
    while base_belt :
        if base_belt[-1] != order[0] :
            sub_belt.append(base_belt.pop())
        else :
            break
    
    for o in order :
        if base_belt and base_belt[-1] == o :
            truck.append(base_belt.pop())
        elif sub_belt and sub_belt[-1] == o :
            truck.append(sub_belt.pop())
        else : 
            if not base_belt :
                break
            while base_belt :
                sub_belt.append(base_belt.pop())
                if sub_belt[-1] == o :
                    truck.append(sub_belt.pop())
                    break
            
    answer = len(truck)
    return answer
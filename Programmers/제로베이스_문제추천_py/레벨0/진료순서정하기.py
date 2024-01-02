def solution(emergency):
    answer = []
    order = []
    key_dict = {}
    for e in emergency :
        order.append(e)
    order.sort(reverse=True)
    for i in range(len(order)) :
        key_dict[order[i]] = i+1
    
    for e in emergency :
        answer.append(key_dict[e])
    
    
    return answer
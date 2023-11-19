def solution(emergency):
    answer = []
    emergency_list = {}
    tmp = sorted(emergency, reverse=True)

    for i in range (0, len(tmp)) :
        emergency_list[tmp[i]] = i+1
    
    for e in emergency :
        answer.append(emergency_list[e])

    return answer
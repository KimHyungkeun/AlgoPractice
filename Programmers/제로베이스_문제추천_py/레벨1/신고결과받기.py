def solution(id_list, report, k):
    answer = []
    requester_dict = {}
    received_dict = {}
    for id in id_list :
        requester_dict[id] = []
        received_dict[id] = 0
    
    for r in report :
        requester = r.split()[0]
        receiver = r.split()[1]
        if receiver not in requester_dict[requester] :
            requester_dict[requester].append(receiver)
            received_dict[receiver] += 1
    
    for r in requester_dict.values() :
        cnt = 0
        for name in r :
            if received_dict[name] >= k :
                cnt += 1
        answer.append(cnt)
                
    return answer
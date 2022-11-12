def solution(score):
    answer = []
    score_dict = {}
    sort_list = []
    for s in score :
        sort_list.append(s)
    sort_list.sort(key = lambda x : sum(x)/2, reverse=True)
    
    for i in range(len(sort_list)) :
        if sum(sort_list[i])/2 not in score_dict :
            score_dict[sum(sort_list[i])/2] = i+1
    
    for s in score :
        answer.append(score_dict[(sum(s)/2)])
   
    return answer
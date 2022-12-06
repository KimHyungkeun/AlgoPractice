def solution(k, score):
    answer = []
    score_list = []
    
    for s in score :
        score_list.append(s)
        score_list.sort(reverse=True)
        
        if len(score_list) > k :
            score_list.pop()
        
        answer.append(score_list[-1])
    return answer
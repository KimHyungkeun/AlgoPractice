def solution(name, yearning, photo):
    answer = []
    score_dict = {}
    for i in range(len(yearning)) :
        score_dict[name[i]] = yearning[i]
    
    for p in photo :
        tmp = 0
        for name in p :
            if name in score_dict :
                tmp += score_dict[name]
        answer.append(tmp)
    return answer
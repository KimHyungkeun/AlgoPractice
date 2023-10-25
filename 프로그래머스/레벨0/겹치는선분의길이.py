def solution(lines):
    answer = 0
        
    min_point = sorted(lines, key = lambda x : x[0])[0][0]
    max_point = sorted(lines, key = lambda x : x[1], reverse=True)[0][1]
    
    dot_dict = {}
    for i in range(min_point, max_point) :
        dot_dict[(i,i+1)] = 0
    
    for l in lines :
        for j in range(l[0],l[1]) :
            dot_dict[(j,j+1)] += 1
    
    for key in dot_dict.keys() :
        if dot_dict[key] >= 2 :
            answer += 1   

    return answer

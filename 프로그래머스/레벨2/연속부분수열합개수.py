def solution(elements):
    answer = 0
    result = set([])
    origin_length = len(elements)
    elements.extend(elements)
    
    for i in range(1, origin_length+1) :
        for j in range(origin_length) :
            result.add(sum(elements[j:j+i]))
    
    
        
    
    answer = len(result)
    return answer
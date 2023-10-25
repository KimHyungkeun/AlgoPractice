def solution(topping):
    answer = 0
    
    first = set([]) # 왼쪽 파편
    second = {} # 오른쪽 파편
    for t in topping :
        if t in second :
            second[t] += 1
        else :
            second[t] = 1
    
    # 두조각으로 나누어서 first, second 각각 토핑 타입 갯수가 같은지 확인 
    for i in range(len(topping)-1) :
        first.add(topping[i]) # 토핑 종류를 first에 넣음
        second[topping[i]] -= 1 # 토핑 종류갯수를 second에서 제외
        if second[topping[i]] == 0 :  
            del second[topping[i]]
        
        if len(first) == len(second) :
            answer += 1
        
    return answer
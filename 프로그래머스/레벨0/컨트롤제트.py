def solution(s):
    answer = 0
    total = []
    lists = s.split()
    
    for l in lists :
        if l.isalpha() :
            if total :
                total.pop()
        else :
            total.append(int(l))
            
    
    answer = sum(total)
    return answer
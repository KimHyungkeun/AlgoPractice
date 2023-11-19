def solution(my_string):
    save = []
    answer = ''
    
    for s in my_string :
        if s not in save :
            save.append(s)
            answer += s
            
    return answer
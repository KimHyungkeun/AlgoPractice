# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    
    answer = []
    now_num = -1
    
    for i in range(len(arr)) :
        
        if arr[i] == now_num :
            continue
            
        else :
            answer.append(arr[i])
            now_num = arr[i]
    
    return answer
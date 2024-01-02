def solution(arr, delete_list):
    answer = []
    for i in range(len(arr)) :
        if arr[i] in delete_list :
            arr[i] = 0
    
    for a in arr :
        if a != 0 :
            answer.append(a)
    return answer
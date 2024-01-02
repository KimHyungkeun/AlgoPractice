def solution(arr):
    if 2 not in arr :
        answer = [-1]
    else :
        answer = []
        i_arr = []
        for i in range(len(arr)) :
            if arr[i] == 2 :
                i_arr.append(i)
        answer = arr[i_arr[0]:i_arr[-1]+1]
    return answer
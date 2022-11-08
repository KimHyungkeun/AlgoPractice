def solution(array, n):
    answer = 0
    result = []
    replica = []
    
    for a in array :
        result.append((a, abs(a-n)))
    
    result.sort(key = lambda x : x[1])

    while result :
        if not replica :
            replica.append(result.pop(0))
        else :
            if replica[-1][1] == result[0][1] :
                replica.append(result.pop(0))
            else :
                break
                
    replica.sort(key = lambda x : x[0])
    answer = replica[0][0]
    return answer
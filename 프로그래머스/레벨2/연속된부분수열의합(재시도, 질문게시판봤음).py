def solution(sequence, k):
    answer = []
    s,e = 0,0
    last_idx = len(sequence)-1
    total = sequence[s]
    
    while s < last_idx or e < last_idx : 

        if total == k: 
            answer.append([s,e])
            if e+1 <= last_idx :
                total += sequence[e]
                e += 1
            continue
        
        if total < k and e+1 <= last_idx :
            e += 1
            total += sequence[e]
        
        elif total > k and s+1 <= e :
            total -= sequence[s]
            s += 1
        
        else :
            total -= sequence[s]
            s += 1
        
        if total == k and s <= e: 
            answer.append([s,e])
            total -= sequence[s]
            s += 1



    answer.sort(key = lambda x : x[0])
    answer.sort(key = lambda x : x[1] - x[0])
    return answer[0]

# sequence = [1, 2, 3, 4, 5]
# k = 7
# sequence = [1, 1, 1, 2, 3, 4, 5]
# k = 5
# sequence = [2, 2, 2, 2, 2]
# k = 6
# sequence = [1,1,1,1,1]
# k = 5
sequence = [5,5,5,5,5]
k = 5

solution(sequence, k)
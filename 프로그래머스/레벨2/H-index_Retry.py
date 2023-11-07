def solution(citations):
    total = len(citations)
    citations.sort()
    
    h_index = 0
    
    
    for h in range(total+1) :
        h_over_used = 0
        h_under_used = 0
        for i in range(total) :
            if citations[i] >= h :
                h_over_used = total - i
                h_under_used = total - h_over_used
                break

        if h_over_used >= h and h_under_used <= h :
            h_index = max(h_index, h)
        else :
            break
        
    return h_index
# 231201 재시도 성공
def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    top = citations[0]
    for h in range(top, -1, -1) :
        cnt = []
        extra_cnt = []
        for i in range(len(citations)) :
            if citations[i] > h :
                cnt.append(citations[i])
            elif citations[i] == h :
                cnt.append(citations[i])
                extra_cnt.append(citations[i])
            else :
                extra_cnt.append(citations[i])
       
        if len(cnt) >= h and len(extra_cnt) <= h :
            break
        
    return h

citations = [3, 0, 6, 1, 5]
print(solution(citations))

# 11/07
# def solution(citations):
#     total = len(citations)
#     citations.sort()
    
#     h_index = 0
    
    
#     for h in range(total+1) :
#         h_over_used = 0
#         h_under_used = 0
#         for i in range(total) :
#             if citations[i] >= h :
#                 h_over_used = total - i
#                 h_under_used = total - h_over_used
#                 break

#         if h_over_used >= h and h_under_used <= h :
#             h_index = max(h_index, h)
#         else :
#             break
        
#     return h_index
def solution(numlist, n):
    answer = []
    
    sort_list = []
    for i in numlist :
        sort_list.append((i, abs(n-i)))
    sort_list.sort(key = lambda x : x[0], reverse=True)
    sort_list.sort(key = lambda x : x[1])
    
    for s in sort_list :
        answer.append(s[0])
    return answer
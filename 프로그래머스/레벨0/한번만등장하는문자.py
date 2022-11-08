def solution(s):
    answer = ''
    cnt_dict = {}
    result = []
    
    for w in s :
        if w not in cnt_dict :
            cnt_dict[w] = 1
        else :
            cnt_dict[w] += 1
    
    str_list = sorted(cnt_dict.items(), key = lambda item : item[1], reverse=True)
    
    while str_list :
        if str_list[-1][1] == 1 :
            result.append(str_list.pop())
        else :
            break
    
    result.sort(key = lambda x : x[0])
    for r in result :
        answer += r[0]
    
    return answer
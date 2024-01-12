def solution(new_id):
    answer = ''
    
    # 1단계
    new_str = new_id.lower()
    
    # 2단계
    str_list = list(new_str)
    for i in range(len(str_list)) :
        if "a" <= str_list[i] <= "z" :
            continue
        if "0" <= str_list[i] <= "9" :
            continue
        if str_list[i] in ["-", "_", "."] :
            continue
        
        str_list[i] = "" 
    new_str = "".join(str_list)
    
    # 3단계
    str_list = list(new_str)
    for i in range(len(str_list)) :
        if i != len(str_list)-1 and str_list[i] == "." :
            for j in range(i+1, len(str_list)) :
                if str_list[j] == "." :
                    str_list[j] = ""
                else :
                    break
        
    new_str = "".join(str_list)
    
    # 4단계
    str_list = list(new_str)
    if str_list[0] == "." :
        str_list[0] = ""
    if str_list[-1] == "." :
        str_list[-1] = ""
    new_str = "".join(str_list)
    
    # 5단계
    if not new_str :
        new_str = "a"
    
    # 6단계
    if len(new_str) >= 16 :
        new_str = new_str[:15]
    r_idx = -1
    while new_str[r_idx] == "." :
        r_idx -= 1
    new_str = new_str[:len(new_str) + r_idx + 1]
    
    # 7단계
    if len(new_str) <= 2 :
        while len(new_str) < 3 :
            new_str += new_str[-1]
    
    answer = new_str
    return answer
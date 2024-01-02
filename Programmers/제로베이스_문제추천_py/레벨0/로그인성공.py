def solution(id_pw, db):
    answer = ''
    key_dict = {}
    for d in db :
        key_dict[d[0]] = d[1]
    
    if id_pw[0] in key_dict :
        if id_pw[1] == key_dict[id_pw[0]] :
            answer = "login"
        else :
            answer = "wrong pw"
    else :
        answer = "fail"
        
    return answer
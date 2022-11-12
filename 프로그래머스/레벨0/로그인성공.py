def solution(id_pw, db):
    answer = ''
    
    db_dict = {}
    for record in db :
        if record[0] not in db_dict :
            db_dict[record[0]] = record[1]
    
    if id_pw[0] not in db_dict :
        answer = "fail"
    elif id_pw[1] == db_dict[id_pw[0]] :
        answer = "login"
    else :
        answer = "wrong pw"
    return answer
def solution(spell, dic):
    
    for d in dic :
        match = 0
        remember = []
 
        for cha in d :
            if cha in spell and cha not in remember:
                match += 1
                remember.append(cha)
            if match == len(spell) :
                return 1
        
    return 2
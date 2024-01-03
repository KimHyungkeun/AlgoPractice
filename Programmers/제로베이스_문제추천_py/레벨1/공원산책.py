def solution(park, routes):
    row = len(park[0])
    col = len(park)
    
    for i in range(len(park)) :
        for j in range(len(park[i])) :
            if park[i][j] == 'S' :
                break
        if park[i][j] == 'S' :
            break
    
    start_i, start_j = i,j
    
    for r in routes :
        cmd = r.split()
        distance = int(cmd[1])
        flag = True
        
        if cmd[0] == 'E' :   
            if j + distance < row :
                for go in range(j, j+distance+1) :
                    if park[i][go] == 'X' :
                        flag = False
                        break
                        
                if not flag :
                    continue
                else :
                    j += distance
                
        if cmd[0] == 'S' :
            if i + distance < col :
                for go in range(i, i+distance+1) :
                    if park[go][j] == 'X' :
                        flag = False
                        break
                        
                if not flag :
                    continue
                else :
                    i += distance
                
        if cmd[0] == 'W' :
            if j - distance >= 0 :
                for go in range(j, j-distance-1, -1) :
                    if park[i][go] == 'X' :
                        flag = False
                        break
                        
                if not flag :
                    continue
                else :
                    j -= distance
                
        if cmd[0] == 'N' :
            if i - distance >= 0 :
                for go in range(i, i-distance-1, -1) :
                    if park[go][j] == 'X' :
                        flag = False
                        break
                        
                if not flag :
                    continue
                else :
                    i -= distance
    
    answer = [i,j]
    return answer
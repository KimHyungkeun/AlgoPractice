def solution(wallpaper):
    answer = [0,0,0,0]
    row = len(wallpaper)
    col = len(wallpaper[0])
    
    # 1. 첫번째 #이 나오는 row
    for i in range(row) :
        if '#' in wallpaper[i] :
            break
    answer[0] = i
    
    # 2. 첫번째 #이 나오는 col
    isFind = False
    for i in range(col) :
        for j in range(row) :
            if wallpaper[j][i] == '#' :
                isFind = True
                break
        if isFind :
            break
    answer[1] = i
        
    
    # 3. 마지막 #이 나오는 row+1
    for i in range(row-1, -1, -1) :
        if '#' in wallpaper[i] :
            break
    answer[2] = i+1
    
    # 4. 마지막 #이 나오는 col+1
    isFind = False
    for i in range(col-1, -1 ,-1) :
        for j in range(row-1, -1, -1) :
            if wallpaper[j][i] == '#' :
                isFind = True
                break
        if isFind :
            break
    answer[3] = i+1
    
    return answer
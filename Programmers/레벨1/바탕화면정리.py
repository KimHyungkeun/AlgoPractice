def solution(wallpaper):
    answer = [0,0,0,0]
    for i in range(len(wallpaper)) :
        wallpaper_list = list(wallpaper[i])
        if '#' in wallpaper_list :
            answer[0] = i
            break
    for i in range(len(wallpaper)-1, -1, -1) :
        wallpaper_list = list(wallpaper[i])
        if '#' in wallpaper_list :
            answer[2] = i+1
            break 
    
    row_length = len(wallpaper[0])
    
    flag = False
    for i in range(row_length) :
        for j in range(len(wallpaper)) :
            if wallpaper[j][i] == '#' :
                answer[1] = i
                flag = True
                break
        if flag :
            break
    
    flag = False
    for i in range(row_length-1, -1, -1) :
        for j in range(len(wallpaper)) :
            if wallpaper[j][i] == '#' :
                answer[3] = i+1
                flag = True
                break
        if flag :
            break
    
        
    return answer
def solution(n):
    answer = [[]]
    board = []
    direction = "right"
    num = 0
    for _ in range(n) :
        board.append([0]*n)
    
    i = 0
    j = 0
    while num < n*n :
        num += 1
        
        if direction == "right" :
            board[i][j] = num
            j += 1
            if j >= n or board[i][j] != 0 :
                direction = "down"
                i += 1
                j -= 1
                continue
                
        
        if direction == "down" :
            board[i][j] = num
            i += 1
            if i >= n or board[i][j] != 0 :
                direction = "left"
                i -= 1
                j -= 1
                continue
        
        if direction == "left" :
            board[i][j] = num
            j -= 1
            if j < 0 or board[i][j] != 0 :
                direction = "up"
                j += 1
                i -= 1
                continue
        
        if direction == "up" :
            board[i][j] = num
            i -= 1
            if i < 0 or board[i][j] != 0 :
                direction = "right"
                i += 1
                j += 1
                continue
        

    
    answer = board
    return answer
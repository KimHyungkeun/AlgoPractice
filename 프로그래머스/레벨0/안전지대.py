def solution(board):
    answer = 0
    size = len(board)**2
    search = []
    
    def bfs (x,y, length, search, answer) :
        dx = [1,-1,0,0,1,-1,1,-1]
        dy = [0,0,1,-1,1,-1,-1,1]
        
        if (x,y) not in search :
            search.append((x,y))
            answer += 1
        
        for i in range(8) :
            px = x + dx[i]
            py = y + dy[i]
            
            if px < 0 or px >= length or py < 0 or py >= length :
                continue
            if (px,py) not in search :
                search.append((px, py))
                answer += 1
                
        return answer
        
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            if board[i][j] == 1 :
                answer = bfs(i,j, len(board[j]), search, answer)
   
    return size - answer
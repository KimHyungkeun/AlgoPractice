from collections import deque
def solution(board):
    cnt = 1
    start = []
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    is_find = False
    row_length = len(board[0])
    
    # 시작점 찾기
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            if board[i][j] == 'R' :
                start = [i,j]
                break
        if start :
            break
    
    visited = [(start[0], start[1])]
    q = deque(visited)
    depth_case_cnt = len(q)
    
    # 탐색시작
    while q :
        y, x = q.popleft()
        depth_case_cnt -= 1
        
        for i in range(4) :
            pos_y = y + dy[i]
            pos_x = x + dx[i]
            
            if pos_x < 0 or pos_x >= row_length or pos_y < 0 or pos_y >= len(board) or board[pos_y][pos_x] == 'D' : 
                continue
            
            if dy[i] == 1 :
                while True :                 
                    if pos_y+1 >= len(board) or board[pos_y+1][pos_x] == 'D' :
                        break    
                    pos_y += 1        
            elif dy[i] == -1 :
                while True :                  
                    if pos_y-1 < 0 or board[pos_y-1][pos_x] == 'D' :
                        break       
                    pos_y -= 1  
            elif dx[i] == 1 :
                while True :
                    if pos_x+1 >= row_length or board[pos_y][pos_x+1] == 'D' :
                        break    
                    pos_x += 1         
            elif dx[i] == -1 :
                while True :
                    if pos_x-1 < 0 or board[pos_y][pos_x-1] == 'D' :
                        break
                    pos_x -= 1
                       
            if (pos_y, pos_x) not in visited :
                visited.append((pos_y, pos_x))
                q.append((pos_y, pos_x))
            
            # 목적지를 찾으면 탐색 종료
            if board[pos_y][pos_x] == 'G' :
                is_find = True
                break
        
        if is_find :
            break

        if depth_case_cnt == 0 :
            cnt += 1
            depth_case_cnt = len(q)
                

        
    
    if is_find :
        return cnt
    else :
        return -1

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
# board = [".D.R", "....", ".G..", "...D"]
print(solution(board))
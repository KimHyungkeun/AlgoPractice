# BFS
from collections import deque
def solution(maps):
    answer = []   
    memory = []
    def bfs(i, j, memory, maps) :
        q = deque([(i,j)])
        memory.append((i,j))
        total = int(maps[i][j])
        
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        while q :
            x, y = q.popleft()
            for i in range(4) :
                change_x = x + dx[i]
                change_y = y + dy[i]
                
                # maps[0]은 가로길이로 측정할 기준을 임의로 고르기위해 선택 하였음
                if change_x < 0 or change_x >= len(maps) or change_y < 0 or change_y >= len(maps[0]) :
                    continue
                if (change_x, change_y) in memory :
                    continue
                if maps[change_x][change_y] == 'X' :
                    memory.append((change_x, change_y))
                    continue
                total += int(maps[change_x][change_y])
                memory.append((change_x, change_y))
                q.append((change_x, change_y))
                
        return total       
                  
    for i in range(len(maps)) :
        for j in range(len(maps[i])) :
            if (i,j) in memory :
                continue
            if maps[i][j] != 'X' :
                val = bfs(i, j, memory, maps)
                answer.append(val)
                
    
    if not answer :
        answer = [-1]
    else :
        answer.sort()
    
    return answer

# maps = ["X591X","X1X5X","X231X", "1XXX1"]
maps = ["XXX","XXX","XXX"]
solution(maps)

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
board = []
for _ in range(n) :
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)

visited = []

def bfs (i, j) :
    is_clear = False
    q = deque([(i,j)])

    while q :
        y,x = q.popleft()

        if board[y][x] == -1 :
            is_clear = True
            return is_clear
                
        if (y,x) not in visited :
            visited.append((y, x))
        
       
        ry = y + board[y][x]
        if 0 <= ry < n :
            if (ry, x) not in visited :
                q.append((ry,x))
        
        rx = x + board[y][x]
        if 0 <= rx < n :
            if (y, rx) not in visited :
                q.append((y,rx))
                         
    return is_clear

if bfs(0,0) :
    print("HaruHaru")
            
else :
    print("Hing")




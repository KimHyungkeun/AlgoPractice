import sys

while True :
    r, c = map(int, sys.stdin.readline().split())
    if r == 0 and c == 0 :
        break
    
    di = [0,0,1,-1,1,1,-1,-1] 
    dj = [1,-1,0,0,1,-1,1,-1]

    result = [[0] * c for _ in range(r)]
    board = []
    for _ in range(r) :
        row = list(sys.stdin.readline().rstrip())
        board.append(row)
    
    for i in range(r) :
        for j in range(c) :
            if board[i][j] == '*' :
                for d in range(8) :
                    if (0 <= i + di[d] < r) and (0 <= j + dj[d] < c) :
                        if board[i+di[d]][j+dj[d]] != '*' : 
                            result[i+di[d]][j+dj[d]] += 1

    for i in range(r) :
        for j in range(c) :
            if board[i][j] == '*' :
                print(board[i][j], end='')
            else :
                print(result[i][j], end='')
        print()
    


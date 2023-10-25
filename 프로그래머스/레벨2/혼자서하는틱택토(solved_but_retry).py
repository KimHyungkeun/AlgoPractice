def solution(board):
    # 1. O의 갯수가 X의 갯수와 같거나 또는 O의 갯수가 X의 갯수보다 1개 많아야 한다
    cnt_o = 0
    cnt_x = 0
    for b in board :
        for mark in b :
            if mark == 'O' :
                cnt_o += 1
            if mark == 'X' :
                cnt_x += 1
    
    if cnt_o - cnt_x != 0 and cnt_o - cnt_x != 1:
        return 0

    # 2. O가 빙고인데 X도 빙고일 수는 없다
    bingo_o = 0
    bingo_x = 0

    # 2-1) 가로빙고
    for row in board :
        row = list(set(row))
        if len(row) == 1 :
            if row[0] == 'O' :
                bingo_o += 1
            if row[0] == 'X' :
                bingo_x += 1
            
    # 2-2) 세로빙고
    for i in range(len(board)) :
        col = []
        for j in range(len(board)) :
            col.append(board[j][i])
        col = list(set(col))
        if len(col) == 1 :
            if col[0] == 'O' :
                bingo_o += 1
            if col[0] == 'X' :
                bingo_x += 1

    # 2-3) 대각선 빙고
    diagon_bingo1 = [board[0][0], board[1][1], board[2][2]]
    diagon_bingo2 = [board[0][2], board[1][1], board[2][0]]
    diagon_bingo1 = list(set(diagon_bingo1))
    diagon_bingo2 = list(set(diagon_bingo2))

    if len(diagon_bingo1) == 1 :
        if diagon_bingo1[0] == 'O' :
            bingo_o += 1
        if diagon_bingo1[0] == 'X' :
            bingo_x += 1

    if len(diagon_bingo2) == 1 :
        if diagon_bingo2[0] == 'O' :
            bingo_o += 1
        if diagon_bingo2[0] == 'X' :
            bingo_x += 1

    if bingo_o > 0 and bingo_x > 0 :
        return 0
    
    # 3. O빙고가 나왔는데 X의 갯수가 O 이상일 경우 유효하지 않다
    if bingo_o > 0 and cnt_o <= cnt_x :
        return 0

    # 4. X빙고가 나왔는데 X의 갯수와 O의 갯수가 같지 않을 경우 유효하지 않다
    if bingo_x > 0 and cnt_o != cnt_x :
        return 0
    
    return 1

board = ["XOX","OO.",".OX"]
print(solution(board))
def solution(board):
    answer = 0
    dx = [0,0,1,-1,1,1,-1,-1]
    dy = [1,-1,0,0,-1,1,1,-1]
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            if board[i][j] == 1 :
                for d in range(8) :
                    ch_i = i + dx[d]
                    ch_j = j + dy[d]
                    if ch_i < 0 or ch_i >= len(board) or ch_j < 0 or ch_j >= len(board) :
                        continue
                    if board[ch_i][ch_j] == 0 :
                        board[ch_i][ch_j] = -1
        
    for b in board :
        answer += b.count(0)
        
    return answer
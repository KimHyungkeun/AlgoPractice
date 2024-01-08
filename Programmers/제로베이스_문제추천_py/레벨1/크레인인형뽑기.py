def solution(board, moves):
    answer = 0
    
    stack = []
    length = len(board[0])
    
    for m in moves :
        i = m-1
        for j in range(length) :
            if board[j][i] != 0 :
                stack.append(board[j][i])
                board[j][i] = 0
                break
        
        while len(stack) >= 2 :
            if len(stack) >= 2 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
            else :
                break
                
    return answer
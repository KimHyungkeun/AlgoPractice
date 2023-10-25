def solution(keyinput, board):

    pos = [0, 0]

    for key in keyinput:
        if key == "left":
            if pos[0] - 1 >= -(board[0]//2):
                pos[0] -= 1
        elif key == "right":
            if pos[0] + 1 <= board[0]//2:
                pos[0] += 1
        elif key == "up":
            if pos[1] + 1 <= board[1]//2:
                pos[1] += 1
        else:
            if pos[1] - 1 >= -(board[1]//2):
                pos[1] -= 1

    return pos

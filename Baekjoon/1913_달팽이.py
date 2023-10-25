import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
total = n**2
max_n = n**2
idx = 0

board = []
for _ in range(n) :
    tmp = [0] * n 
    board.append(tmp)
direction = deque(["down", "right", "up", "left"])

i,j = 0,0
k_i, k_j = 0,0

while idx < total :
    board[i][j] = max_n

    if k == max_n :
        k_i, k_j = i, j

    max_n -= 1

    if direction[0] == "down" :
        if i + 1 >= n or board[i + 1][j] != 0 :
            direction.append(direction.popleft())
        else :
            i += 1
    
    if direction[0] == "right" :
        if j + 1 >= n or board[i][j + 1] != 0 :
            direction.append(direction.popleft())
        else :
            j += 1

    if direction[0] == "up" :
        if i - 1 < 0 or board[i - 1][j] != 0 :
            direction.append(direction.popleft())
        else :
            i -= 1
    
    if direction[0] == "left" :
        if j - 1 < 0 or board[i][j - 1] != 0 :
            direction.append(direction.popleft())
            i += 1
        else :
            j -= 1
    
    idx += 1


for b in board :
    for n in b :
        print(n, end=' ')
    print()
print(k_i + 1, k_j + 1)
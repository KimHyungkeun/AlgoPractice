import sys 

M, n = map(int, sys.stdin.readline().split())


# 0: 동, 1: 북, 2: 서, 3: 남
direction = 0
start = [0, M]
for _ in range(n) :
    is_valid = True
    cmd, num = sys.stdin.readline().split()

    if cmd == "MOVE" :
        if direction == 0 :
            start[0] += int(num) 
        if direction == 1 :
            start[1] -= int(num)
        if direction == 2 :
            start[0] -= int(num)
        if direction == 3 :
            start[1] += int(num)

        if start[0] < 0 or start[0] >= M+1 or start[1] < 0 or start[1] >= M+1 :
            is_valid = False
            break
        
    if cmd == "TURN" :
        if num == "0" :
            direction = ((int(direction)+1) % 4)
        if num == "1" :
            direction = ((int(direction)-1) % 4)

if is_valid :
    print(start[0], M - start[1])
else :
    print(-1)

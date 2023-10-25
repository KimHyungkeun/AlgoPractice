import sys

board = []
for _ in range(501) :
    board.append([0]*501)

n = int(sys.stdin.readline().rstrip())

for _ in range(n) :
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for i in range(y1, y2) :
        for j in range(x1, x2) :
            board[i][j] = 1

cnt = 0
for b in board :
    cnt += sum(b)


print(cnt)



import sys

board = []
for _ in range(101) :
    board.append([0]*101)

n, m = map(int, sys.stdin.readline().split())

# x1, y1, x2, y2 좌표를 입력받고, 입력된 영역에 해당하는 곳에 그림을 덧붙인다
for _ in range(n) :
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for i in range(y1, y2+1) :
        for j in range(x1, x2+1) :
            board[i][j] += 1
            
# m개를 초과한 그림에 대해서는 보이지 않게 된다
cnt = 0
for row in board :
    for r in row :
        if r > m :
            cnt += 1

print(cnt)
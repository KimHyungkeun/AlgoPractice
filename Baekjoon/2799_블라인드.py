import sys

m, n = map(int, sys.stdin.readline().split())
shadow = {0:0, 1:0, 2:0, 3:0, 4:0} # 블라인드로 가려지는 경우의 수 : 0*4, 1*4, 2*4, 3*4, 4*4
windows = []
for _ in range(5*m + 1) :
    board = list(sys.stdin.readline().rstrip())
    windows.append(board)

for i in range(1, 5*m+1, 5) : 
    for j in range(1, 5*n+1, 5) :
        cnt = 0
        for k in range(i, i+4) :
            if windows[k][j] == '*' :
                cnt += 1
                if cnt == 4 :
                    shadow[cnt] += 1
                    break
            else :
                shadow[cnt] += 1
                break


for val in shadow.values() :  
    print(val, end = ' ')
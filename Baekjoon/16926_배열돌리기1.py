# 참고 : https://velog.io/@gkscodus11/%EB%B0%B1%EC%A4%80-16926-%EB%B0%B0%EC%97%B4-%EB%8F%8C%EB%A6%AC%EA%B8%B0-1
import sys
from collections import deque

n, m, r  = map(int, sys.stdin.readline().split())
board = []

for _ in range(n) :
    tmp = list(map(int, sys.stdin.readline().split()))
    board.append(tmp)

start_i = 0
start_j = 0
while True :
    q = deque([])

    # 시계 반대방향으로 돌아가면서 값을 추출함
    for j in range(start_j, m) :
        q.append(board[start_i][j])
    for i in range(start_i+1, n) :
        q.append(board[i][m-1])
    for j in range(m-2, start_j-1, -1) :
        q.append(board[n-1][j])
    for i in range(n-2, start_i, -1) :
        q.append(board[i][start_j])
    

    # 반시계방향으로 r번 밀리게 함
    for _ in range(r) :
        q.append(q.popleft())

    # 시계 반대방향으로 돌아가면서 새로운 값으로 갱신
    while q: 
        for j in range(start_j, m) :
            board[start_i][j] = q.popleft()
        for i in range(start_i+1, n) :
            board[i][m-1] = q.popleft()
        for j in range(m-2, start_j-1, -1) :
            board[n-1][j] = q.popleft()
        for i in range(n-2, start_i, -1) :
            board[i][start_j] = q.popleft()
    
    start_i += 1
    start_j += 1
        
    n -= 1
    m -= 1

    if n - start_i < 2 or m - start_j < 2 :
        break



for i in range(len(board)) :
    for j in range(len(board[i])) :
        print(board[i][j], end=' ')
    print()



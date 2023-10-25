import sys

r, c = map(int, sys.stdin.readline().split())
board = []

for _ in range(r) :
    num_list = list(map(int, sys.stdin.readline().split()))
    board.append(num_list)

t = int(sys.stdin.readline().rstrip())

center_list = []
for i in range(r-2) :
    nums = []
    # nums 배열 중 크기 중간인 값을 구함
    for j in range(c-2) :
        nums = [board[i][j],board[i][j+1],board[i][j+2],board[i+1][j],board[i+1][j+1],board[i+1][j+2],board[i+2][j],board[i+2][j+1],board[i+2][j+2]]
        nums.sort()
        center_list.append(nums[4]) 

cnt = 0
for val in center_list :
    if val >= t :
        cnt += 1

print(cnt)


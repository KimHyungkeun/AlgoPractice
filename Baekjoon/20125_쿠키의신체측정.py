import sys

n = int(sys.stdin.readline().rstrip())
board = []

# 머리 위치
head_pos = []

is_first_head = False
for i in range(n) :
    row = list(sys.stdin.readline().rstrip())
    if not is_first_head and '*' in row :
        is_first_head = True
        head_pos = [i, row.index('*')]
    board.append(row)


# 심장 위치 = 머리 위치 바로 1칸 아래
heart_i = head_pos[0]+1
heart_j = head_pos[1]
print(heart_i+1, heart_j+1)

# 왼쪽 팔 길이 = 심장위치에서 왼쪽 '*' 갯수 (심장위치의 '*'은 제외)
left_arm = 0
for j in range(heart_j-1, -1, -1) :
    if board[heart_i][j] == '*' :
        left_arm += 1
    if board[heart_i][j] != '*' :
        break
print(left_arm, end=' ')

# 오른쪽 팔 길이 = 심장위치에서 오른쪽 '*' 갯수 (심장위치의 '*'은 제외)
right_arm = 0
for j in range(heart_j+1, n) :
    if board[heart_i][j] == '*' :
        right_arm += 1
    if board[heart_i][j] != '*' :
        break
print(right_arm, end=' ')

# 허리 길이 = 심장위치에서 아래쪽 '*' 갯수 (심장위치의 '*'은 제외)
back = 0
for i in range(heart_i+1, n) :
    if board[i][heart_j] == '*' :
        back += 1
    if board[i][heart_j] != '*' :
        i -= 1
        break
back_pos = [i, heart_j]
print(back, end=' ')

# 왼쪽 다리 길이 => 허리 끝부분에서 왼쪽 대각선 방향 (i+1,j-1) 위치가 시작 부분. 이곳을 시작으로 길이 구함  
left_leg = 0
left_leg_i = back_pos[0] + 1
left_leg_j = back_pos[1] - 1

for i in range(left_leg_i, n) :
    if board[i][left_leg_j] == '*' :
        left_leg += 1
    if board[i][left_leg_j] != '*' :
        break
print(left_leg, end=' ')

# 오른쪽 다리 길이 => 허리 끝부분에서 오른쪽 대각선 방향 (i+1,j+1) 위치가 시작 부분. 이곳을 시작으로 길이 구함
right_leg = 0
right_leg_i = back_pos[0] + 1
right_leg_j = back_pos[1] + 1

for i in range(right_leg_i, n) :
    if board[i][right_leg_j] == '*' :
        right_leg += 1
    if board[i][right_leg_j] != '*' :
        break
print(right_leg, end=' ')
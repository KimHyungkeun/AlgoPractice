from collections import deque
import sys

cur_pos = 0
sec = 0
n, l = map(int, sys.stdin.readline().split())
signal_pos = []

# d : 신호등 위치
# 1번째 [r,g] : 신호등이 바뀌기까지의 경과 시간
# 2번째 [r,g] : 각 신호등별 최대 켜져있는 시간을 기억
# True/False : True이면 초록불, False이면 빨간불 상태
for _ in range(n) :
    d, r, g = map(int, sys.stdin.readline().split())
    signal_pos.append([d, [r,g], [r,g], False])

q = deque(signal_pos)

save = 0
is_pending = False
while cur_pos < l :
    sec += 1

    if not is_pending :
        cur_pos += 1

    if q :
        for signal_info in q :
            if signal_info[3] == False :
                signal_info[1][0] -= 1
            
            if signal_info[3] == True :
                signal_info[1][1] -= 1

    # 신호등 위치에 왔지만, 아직 빨간불일 경우
    if q :
        if q[0][0] == cur_pos and q[0][1][0] > 0 :
            is_pending = True

    # 신호등 위치에 왔고, 빨간불이 시간이 다 한 경우
    if q : 
        if q[0][0] == cur_pos and q[0][1][0] == 0 :
            is_pending = False
            q.popleft()
    
    # 현재 초록불일 경우
    if q :
        if q[0][3] == True :
            is_pending = False
            q.popleft()
            
    # 초록불이 다하면 빨간불 모드로, 빨간불이 다하면 초록불 모드로 변환
    if q :   
        for signal_info in q :
            if signal_info[1][0] == 0 :
                signal_info[1][0] = signal_info[2][0]
                signal_info[3] = True
            
            if signal_info[1][1] == 0 :
                signal_info[1][1] = signal_info[2][1]
                signal_info[3] = False

print(sec)
import sys

n, m = map(int, sys.stdin.readline().split())
roadway = [0] * 101
player = [0] * 101
point_area = []

# 도로별 제한속도 구간 
start = 0
for _ in range(n) :
    area, speed = map(int, sys.stdin.readline().split())
    for i in range(start, start+area+1) :
        roadway[i] = speed
    point_area.append(start)
    start += area
    
# 운전자가 구역별로 달렸던 속도
start = 0
for _ in range(m) :
    area, speed = map(int, sys.stdin.readline().split())
    for i in range(start, start+area+1) :
        player[i] = speed
    start += area

# 넘긴 제한속도 리스트 중, 가장 최고속도로 달렸을때의 속도값을 구한다
max_exceed = 0
for i in range(101) :
    if player[i] > roadway[i] and player[i] - roadway[i] > max_exceed :
        max_exceed = player[i] - roadway[i]
                
print(max_exceed)   
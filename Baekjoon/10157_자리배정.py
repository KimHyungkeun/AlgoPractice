import sys 
from collections import deque

c, r = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline().rstrip())

# 번호 k가 좌석 총 개수를 초과하면 0으로 출력
if k > c * r :
    print(0)

else :
    consert_seat = []
    direction = deque(["up", "right", "down", "left"])

    for _ in range(r) :
        tmp = [0] * c
        consert_seat.append(tmp)

    start_num = 1
    y, x = r-1, 0
    real_x, real_y = 1,1

    # 위, 오른, 아래, 왼 순서대로 총 좌석 갯수의 횟수만큼 반복
    idx = 0    
    while idx < c * r :    
        consert_seat[y][x] = start_num

        if start_num == k :
            break

        start_num += 1
        if direction[0] == "up" :
            y -= 1
            real_y += 1
            if y - 1 < 0 or consert_seat[y-1][x] != 0:
                direction.append(direction.popleft())

        elif direction[0] == "right" :
            x += 1  
            real_x += 1
            if x + 1 >= c or consert_seat[y][x+1] != 0:
                direction.append(direction.popleft())

        elif direction[0] == "down" :
            y += 1
            real_y -= 1
            if y + 1 >= r or consert_seat[y+1][x] != 0:
                direction.append(direction.popleft())
        else :
            x -= 1
            real_x -= 1
            if x - 1 < 0 or consert_seat[y][x-1] != 0:
                direction.append(direction.popleft())

        idx += 1

    print(real_x, real_y)

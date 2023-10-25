import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
total_wide = 0
field_type = {'a' : [4,2,3,1,3,1], 
              'b' : [4,2,3,1,4,1], 
              'c' : [4,2,4,2,3,1],
              'd' : [4,2,3,2,3,1]}
side_type = {}

direction_list = deque([])
length_list = deque([])

for _ in range(6) :
    direction, length = map(int, sys.stdin.readline().split())
    direction_list.append(direction)
    length_list.append(length)
    if direction not in side_type :
        side_type[direction] = length
    else :
        side_type[direction] += length

# total 면적 구하기 (직사각형 기준)
sorted_side = sorted(side_type.values(), reverse=True)
total_wide = sorted_side[0] * sorted_side[2]

while True :
    isFound = False
    for key in field_type.keys() :
        if list(direction_list) == field_type[key] :
            isFound = True
            break
    if isFound :
        break

    direction_list.appendleft(direction_list.pop())
    length_list.appendleft(length_list.pop())

# 참외 밭 모양별 제외해야할 부분의 넓이
if key == 'a' :
    except_wide = length_list[3] * length_list[4]
if key == 'b' :
    except_wide = length_list[4] * length_list[5]
if key == 'c' :
    except_wide = length_list[1] * length_list[2]
if key == 'd' :
    except_wide = length_list[2] * length_list[3]

print(n * (total_wide - except_wide))
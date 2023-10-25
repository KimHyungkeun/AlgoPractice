import sys

len_n1, len_n2 = map(int, sys.stdin.readline().split())
n1 = list(sys.stdin.readline().rstrip())
n2 = list(sys.stdin.readline().rstrip())
t = int(sys.stdin.readline().rstrip())

road = []

for i in range(len_n1-1, -1, -1) :
    road.append((n1[i], 'l'))
for i in range(len_n2) :
    road.append((n2[i], 'r'))


# 서로 반대방향의 개미를 만나면 위치를 swap 시킨다
for _ in range(t) :
    jump = 0
    for i in range(len(road)-1) :
        if road[i][1] == 'l' and road[i+1][1] == 'r' :
            jump += 1
    
    for i in range(len(road)-1) :
        if road[i][1] == 'l' and road[i+1][1] == 'r' :
            road[i], road[i+1] = road[i+1], road[i]
            jump -= 1

        if jump == 0 :
            break
        else :
            continue
    
result = ""
for r in road :
    result += r[0]

print(result)


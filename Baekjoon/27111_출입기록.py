import sys

n = int(sys.stdin.readline().rstrip())
inside = {}

cnt = 0
for _ in range(n) :
    person, in_out = map(int, sys.stdin.readline().split())
    if in_out == 1 :
        if person in inside :
            cnt += 1
        else :
            inside[person] = True
    if in_out == 0 :
        if person not in inside :
            cnt += 1
        else :
            del inside[person]

# 기록상의 누락횟수 + 부대내에 아직 남아있는 사람 수
print(cnt + len(inside))

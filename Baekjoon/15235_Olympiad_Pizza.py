import sys

n = int(sys.stdin.readline().rstrip())
contestant = list(map(int, sys.stdin.readline().split()))
result = []

cnt = 0
while sum(contestant) != 0 :
    for i in range(len(contestant)) :
        if contestant[i] != 0 :
            cnt += 1
            contestant[i] -= 1
            if contestant[i] == 0 :
                result.append((i, cnt))
        
result.sort(key = lambda x : x[0])

for r in result :
    print(r[1], end=' ')
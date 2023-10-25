import sys

h, w = map(int, sys.stdin.readline().split())
weather = []
result = []
for _ in range(h) :
    cloud = list(sys.stdin.readline().rstrip())
    weather.append(cloud)

for i in range(len(weather)) :
    first_cloud_meet = False
    tmp = []
    for j in range(len(weather[i])) :
        if not first_cloud_meet and weather[i][j] == '.' :
            tmp.append(-1)
        elif weather[i][j] == 'c' :
            first_cloud_meet = True
            tmp.append(0)
        else :
            tmp.append(tmp[-1] + 1)
    result.append(tmp)

for i in range(len(result)) :
    for j in range(len(result[i])) :
        print(result[i][j], end = ' ')
    print()

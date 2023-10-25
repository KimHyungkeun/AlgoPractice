import sys

arr = []
for _ in range(9) :
    tmp = list(map(int, sys.stdin.readline().split()))
    arr.append(tmp)

max = -1
pos = []
for i in range(9) :
    for j in range(9) :
        if arr[i][j] > max :
            max = arr[i][j]
            pos = [i,j]

print(max)
print(pos[0]+1, pos[1]+1)
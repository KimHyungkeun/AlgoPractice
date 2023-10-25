import sys

n = int(sys.stdin.readline())
point = 9

if n == 1 :
    print(point)
else :
    for _ in range(n-1) :
       point = ((point ** 0.5) + (point ** 0.5 - 1)) ** 2

    print(int(point)) 

import sys

n = int(sys.stdin.readline().rstrip())

x_list = []
y_list = []
for _ in range(n) :
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)

print((max(y_list) - min(y_list)) * (max(x_list) - min(x_list))) 
import sys

side_list = list(map(int, sys.stdin.readline().split()))
side_list.sort(reverse=True)


while side_list[0] >= sum(side_list[1:]) :
    side_list[0] -= 1
    
print(sum(side_list))


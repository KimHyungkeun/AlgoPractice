import sys

while True :
    a,b,c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0 :
        break

    side_list = [a,b,c]
    side_list.sort(reverse=True)

    if side_list[0] >= sum(side_list[1:]) :
        print("Invalid")

    else :
        if len(set(side_list)) == 1 :
            print("Equilateral")

        elif len(set(side_list)) == 2 :
            print("Isosceles")
        
        else :
            print("Scalene")
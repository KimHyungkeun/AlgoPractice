import sys

while True :
    n = int(sys.stdin.readline().rstrip())
    if n == 0 :
        break

    student_list = []
    max_height = 0
    for _ in range(n) :
        name, height = sys.stdin.readline().split()
        student_list.append((name, float(height)))
        if float(height) > max_height :
            max_height = float(height)
    
    for s in student_list :
        if s[1] == max_height :
            print(s[0], end = ' ')
    print()

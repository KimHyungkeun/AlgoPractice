import sys

n = int(sys.stdin.readline().rstrip())

stack = []

for _ in range(n) :
    cmd = sys.stdin.readline().rstrip()

    # 정수를 스택에 넣음
    if cmd.split()[0] == '1' :
        stack.append(int(cmd.split()[1]))
    
    # 스택에 정수가 있다면 맨 위의 정수를 빼고 출력. 없으면 -1 출력
    if cmd.split()[0] == '2' :
        if not stack :
            print(-1)
        else :
            print(stack.pop())
    
    # 스택에 들어있는 정수의 갯수를 출력
    if cmd.split()[0] == '3' :
        print(len(stack))
    
    # 스택이 비어있으면 1, 아니면 0 출력
    if cmd.split()[0] == '4' :
        if not stack :
            print(1)
        else :
            print(0)
    
    # 스택에 정수가 있다면 맨 위츼 정수를 출력. 없다면 -1 출력
    if cmd.split()[0] == '5' :
        if stack :
            print(stack[-1])
        else :
            print(-1)
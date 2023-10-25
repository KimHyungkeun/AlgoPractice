import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

q = deque([])
for _ in range(n) :
    cmd = sys.stdin.readline().rstrip()
    cmd_input_list = cmd.split()
    
    # 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
    if cmd_input_list[0] == '1' :
        q.appendleft(cmd_input_list[1])
    
    # 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
    if cmd_input_list[0] == '2' :
        q.append(cmd_input_list[1])
    
    # 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    if cmd_input_list[0] == '3' :
        if not q :
            print(-1)
        else :
            print(q.popleft())
    
    # 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
    if cmd_input_list[0] == '4' :
        if not q :
            print(-1)
        else :
            print(q.pop())
    
    # 덱에 들어있는 정수의 개수를 출력한다.
    if cmd_input_list[0] == '5' :
        print(len(q))
    
    # 덱이 비어있으면 1, 아니면 0을 출력한다.
    if cmd_input_list[0] == '6' :
        if not q :
            print(1)
        else :
            print(0)
    
    # 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    if cmd_input_list[0] == '7' :
        if q :
            print(q[0])
        else :
            print(-1)
    
    # 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
    if cmd_input_list[0] == '8' :
        if q :
            print(q[-1])
        else :
            print(-1)

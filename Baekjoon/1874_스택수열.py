import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
stack = []
num_list = []
history = []
for _ in range(n) :
    num_list.append(int(sys.stdin.readline().rstrip()))
q = deque(sorted(num_list))

flag = True
for num in num_list :
    # stack이 비어있으면 새로추가
    if not stack :
        stack.append(q.popleft())
        history.append("+")
    
    # stack의 가장 마지막 값이 num과 같으면 stack에서 제외 후, num_list의 다음 값을 평가
    if stack[-1] == num :
        history.append("-")
        q.append(stack.pop())
        continue

    # stack의 가장 마지막 값이 num일때까지 q의 맨 앞 값을 stack에 저장. (q 내부의 내용이 없어질때까지) 
    while q and stack[-1] != num :
        stack.append(q.popleft())
        history.append("+")
    
    # 만약 q가 전부 없어지면, 스택수열로는 num_list 순서대로의 수열을 만드는 것이 불가
    if not q :
        flag = False
        break

    q.append(stack.pop())
    history.append("-")

if flag :
    for h in history :
        print(h)
else :
    print("NO")
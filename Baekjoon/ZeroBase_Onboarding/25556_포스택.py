# https://www.acmicpc.net/problem/25556

import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))

isTrue = True
stack1 = []
stack2 = []
stack3 = []
stack4 = []

for ele in a :
    if not stack1 :
        stack1.append(ele)
    elif stack1[-1] < ele :
        stack1.append(ele) 
    elif not stack2 :
        stack2.append(ele)
    elif stack2[-1] < ele :
        stack2.append(ele)
    elif not stack3 :
        stack3.append(ele)
    elif stack3[-1] < ele :
        stack3.append(ele)
    elif not stack4 :
        stack4.append(ele)
    elif stack4[-1] < ele :
        stack4.append(ele)  
    else :
        isTrue = False
        break

if not isTrue :
    print("NO") 

else :
    while n > 0 :
        if stack1 and stack1[-1] == n :
            stack1.pop()
            n -= 1
        elif stack2 and stack2[-1] == n :
            stack2.pop()
            n -= 1
        elif stack3 and stack3[-1] == n :
            stack3.pop()
            n -= 1
        elif stack4 and stack4[-1] == n :
            stack4.pop()
            n -= 1
        else :
            isTrue = False
            break
    
    if not isTrue :
        print("NO")
    else :
        print("YES") 
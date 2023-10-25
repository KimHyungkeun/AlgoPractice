import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
form = list(sys.stdin.readline().rstrip())
val_dict = {}
stack = []

num_list = []
for _ in range(n) :
    num_list.append(int(sys.stdin.readline().rstrip()))


for i in range(len(form)) :
    if 'A' <= form[i] <= 'Z' or 'a' <= form[i] <= 'z':
        val_dict[form[i]] = ''

idx = 0
for key in val_dict.keys() :
    val_dict[key] = str(num_list[idx])
    idx += 1

for i in range(len(form)) :
    if 'A' <= form[i] <= 'Z' or 'a' <= form[i] <= 'z':
        form[i] = val_dict[form[i]]

q = deque(form)
for f in form :
    if not stack :
        stack.append(f)
    else :
        if f.isdigit() :
            stack.append(f)
        else :
            if f == '+' :
                val = float(stack[-2]) + float(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(str(val)) 
            elif f == '-' :
                val = float(stack[-2]) - float(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(str(val)) 
            elif f == '*' :
                val = float(stack[-2]) * float(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(str(val)) 
            else :
                val = float(stack[-2]) / float(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(str(val)) 

print("{:.2f}".format(float(stack[0])))
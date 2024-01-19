import sys

n, m = map(int, sys.stdin.readline().split())
apple_list = list(map(int, sys.stdin.readline().split()))

apple_list.sort()
for i in range(len(apple_list)) :
    if apple_list[i] <= m :
        m += 1
    else :
        break

print(m)
        

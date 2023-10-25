import sys

n = int(sys.stdin.readline())
name_list = []
for _ in range(n) :
    name_list.append(sys.stdin.readline().rstrip())

asend_list = sorted(name_list)
desc_list = sorted(name_list, reverse=True)

if name_list == asend_list :
    print("INCREASING")
elif name_list == desc_list :
    print("DECREASING")
else :
    print("NEITHER")
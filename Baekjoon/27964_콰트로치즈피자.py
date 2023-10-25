import sys

n = int(sys.stdin.readline().rstrip())

toping_list = list(sys.stdin.readline().split())
cheese_list = []

# 토핑에 치즈가 들어가는 것들을 먼저 골라낸다
for t in toping_list :
    if 'Cheese' in t and t[-6:] == 'Cheese':
        cheese_list.append(t)

# 골라낸 치즈들이 4종류가 맞는지 확인한다
if len(set(cheese_list)) >= 4 :
    print("yummy")
else :
    print("sad")
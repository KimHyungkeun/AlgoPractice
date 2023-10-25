import sys

n = int(sys.stdin.readline().rstrip())
poke_dict = {}

for _ in range(n) :
    poke_name = sys.stdin.readline().rstrip()
    need_candy, total_candy = map(int, sys.stdin.readline().split())

    cnt = 0
    while need_candy <= total_candy :
        total_candy -= need_candy
        total_candy += 2
        cnt += 1
    
    poke_dict[poke_name] = cnt

max_cnt = max(poke_dict.values())
total_cnt = sum(poke_dict.values())

for key in poke_dict.keys() :
    if poke_dict[key] == max_cnt :
        break

print(total_cnt)
print(key)

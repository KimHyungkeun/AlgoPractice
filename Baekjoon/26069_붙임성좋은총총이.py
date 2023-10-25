import sys

n = int(sys.stdin.readline().rstrip())


user_dict = {}
for _ in range(n) :
    a, b = sys.stdin.readline().split()

    # 해당 유저가 list내에 없을시
    if a not in user_dict :
        user_dict[a] = False
    if b not in user_dict :
        user_dict[b] = False
    
    # 해당 유저가 ChongChong이면 True
    if a == "ChongChong" :
        user_dict[a] = True
    if b == "ChongChong" :
        user_dict[b] = True
    
    # 만난 유저가 True이면 본인도 True로 설정
    if user_dict[a] :
        user_dict[b] = True
    if user_dict[b] :
        user_dict[a] = True

cnt = 0
for key in user_dict.keys() :
    if user_dict[key] :
        cnt += 1

print(cnt)
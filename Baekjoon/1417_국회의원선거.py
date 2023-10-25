import sys
n = int(sys.stdin.readline().rstrip())

if n == 1 :
    print(0)

else :
    person1 = int(sys.stdin.readline().rstrip())
    person_list = []
    for _ in range(n-1) :
        person_list.append(int(sys.stdin.readline().rstrip()))
    person_list.sort(reverse=True)

    cnt = 0
    while person1 <= max(person_list) :
        person1 += 1
        person_list[0] -= 1
        person_list.sort(reverse=True)
        cnt += 1
    
    print(cnt)

# 230606 풀이(답봤음)
# import sys
# n = int(sys.stdin.readline().rstrip())

# num_list = []
# for _ in range(n) :
#     num_list.append(int(sys.stdin.readline().rstrip()))

# player_pick = num_list[0]
# num_list.pop(0)
# num_list.sort(reverse=True)

# if n == 1 :
#     print(0)

# else :
#     cnt = 0
#     while player_pick <= max(num_list) :
#         player_pick += 1
#         num_list[0] -= 1
#         cnt += 1
#         num_list.sort(reverse=True)


#     print(cnt)
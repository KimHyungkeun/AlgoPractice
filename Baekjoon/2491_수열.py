# 230628 재풀이
import sys

n = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().split()))

asec = []
desc = []

asec_cnt = 1
for i in range(len(num_list)-1) :
    if num_list[i] <= num_list[i+1] :
        asec_cnt += 1
    else :
        asec.append(asec_cnt)
        asec_cnt = 1
asec.append(asec_cnt)

desc_cnt = 1
for i in range(len(num_list)-1) :
    if num_list[i] >= num_list[i+1] :
        desc_cnt += 1
    else :
        desc.append(desc_cnt)
        desc_cnt = 1
desc.append(desc_cnt)

print(max(max(asec), max(desc)))


# # 힌트 : 오름차순과 내림차순 경우를 나누어서 진행할 것
# n = int(sys.stdin.readline().rstrip())
# num_list = list(map(int, sys.stdin.readline().split()))


# if n <= 2:
#     print(len(num_list))

# else :
#     # 오름차순
#     asc_sort = []
#     # 내림차순
#     desc_sort = []

#     up_cnt = 0
#     down_cnt = 0
#     tmp = [num_list[0], num_list[1]]
#     if tmp[0] <= tmp[1] :
#         up_cnt = 2

#     for i in range(2, n) :
#         tmp[0] = tmp[1]
#         tmp[1] = num_list[i]

#         if tmp[0] <= tmp[1] :
#             up_cnt += 1
#         else :
#             asc_sort.append(up_cnt)
#             up_cnt = 1
#     asc_sort.append(up_cnt)

#     tmp = [num_list[0], num_list[1]]
#     if tmp[0] >= tmp[1] :
#         down_cnt = 2
    
#     for i in range(2, n) :
#         tmp[0] = tmp[1]
#         tmp[1] = num_list[i]

#         if tmp[0] >= tmp[1] :
#             down_cnt += 1
#         else :
#             desc_sort.append(down_cnt)
#             down_cnt = 1
#     desc_sort.append(down_cnt)
    
#     print(max(max(asc_sort), max(desc_sort)))
        





        




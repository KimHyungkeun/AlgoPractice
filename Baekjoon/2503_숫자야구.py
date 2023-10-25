# 230613 재풀이
from itertools import permutations
import sys

n = int(sys.stdin.readline().rstrip())
num_list = [i for i in range(1, 10)]

all_cases = list(permutations(num_list, 3))

for _ in range(n) :
    nums, strike, ball = map(int, sys.stdin.readline().split())
    nums = str(nums)

    idx = 0
    while idx < len(all_cases) :
        s = 0
        b = 0
        for i in range(3) :
            if int(nums[i]) == all_cases[idx][i] :
                s += 1
        
        if int(nums[0]) == all_cases[idx][1] or int(nums[0]) == all_cases[idx][2] :
            b += 1
        
        if int(nums[1]) == all_cases[idx][0] or int(nums[1]) == all_cases[idx][2] :
            b += 1
        
        if int(nums[2]) == all_cases[idx][0] or int(nums[2]) == all_cases[idx][1] :
            b += 1
        
        if s == strike and b == ball :
            idx += 1
        
        else :
            all_cases.remove(all_cases[idx])
            idx = 0

print(len(all_cases))




# from itertools import permutations
# import sys

# n = int(sys.stdin.readline().rstrip())
# num_list = list(permutations([i for i in range(1,10)], 3))

# for _ in range(n) :
#     test,s,b = map(int, sys.stdin.readline().split())
#     test = str(test)

#     idx = 0
#     while idx < len(num_list) :
#         strike = 0
#         ball = 0

#         for i in range(len(test)) :
#             if int(test[i]) == num_list[idx][i] :
#                 strike += 1
#             else :
#                 for j in range(len(test)) :
#                     if i != j and int(test[i]) == num_list[idx][j] :
#                         ball += 1
        
        
#         if strike == s and ball == b :
#             idx += 1
#         else :
#             num_list.remove(num_list[idx])
#             idx = 0

# print(len(num_list))

    



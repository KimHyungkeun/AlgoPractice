# 231001 Retry Success
import sys

def my_round(n) :
    if n - int(n) >= 0.5 :
        return int(n) + 1
    else :
        return int(n)

n = int(sys.stdin.readline().rstrip())

if n == 0 :
    print(0)

else :
    diff_list = []
    for _ in range(n) :
        diff_list.append(int(sys.stdin.readline().rstrip()))

    diff_list.sort()
    top_down_limit = my_round(n * 0.15)

    final_list = diff_list[top_down_limit:n-top_down_limit]

    if len(final_list) == 0 :
        print(0)

    else :
        print(my_round(sum(final_list) / len(final_list)))


# 230927 추후 Retry 필요 
# import sys
# import decimal

# n = int(sys.stdin.readline().rstrip())

# def my_round(n) :
#     if (n - int(n) >= 0.5) :
#         result = int(n) + 1
#     else :
#         result = int(n)
#     return result

# if n == 0 :
#     print(0)

# else :
#     diff_list = []
#     for _ in range(n) :
#         diff_list.append(int(sys.stdin.readline().rstrip()))

#     diff_list.sort()

#     limit_idx = my_round(n * 0.15)

#     diff_list = diff_list[limit_idx:n-limit_idx]

#     print(my_round(sum(diff_list) / len(diff_list)))

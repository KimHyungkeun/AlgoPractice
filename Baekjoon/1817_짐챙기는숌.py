# 230516 재풀이
import sys

n, m = map(int, sys.stdin.readline().split())

if n == 0 :
    print(0)

else :
    bagage = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    box = 0
    for b in bagage :
        if box + b > m :
            cnt += 1
            box = b
        else :
            box += b

    cnt += 1
    print(cnt)




# import sys

# n, m = map(int, sys.stdin.readline().split())

# if n == 0 :
#     print(0)
# else :
#     books = list(map(int, sys.stdin.readline().split()))

#     cnt = 0
#     box = 0
#     for b in books :
#         if box + b > m :
#             box = 0
#             box += b
#             cnt += 1
#         else :
#             box += b

#     if box <= m :
#         box = 0
#         cnt += 1
    
#     print(cnt)
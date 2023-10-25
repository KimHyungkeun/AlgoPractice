# 231024 재시도
import sys

n = int(sys.stdin.readline().rstrip())

def recursion(n, frm, otr, to) :
    if n == 1 :
        print(frm, to)
    else :
        recursion(n-1, frm, to, otr)
        print(frm, to)
        recursion(n-1, otr, frm, to)

print(2**n-1)
recursion(n, 1, 2, 3)

# 231020 재시도
# import sys

# # frm : 시작하려는 장대번호
# # otr : 나머지 남은 장대번호
# # to : 최종적으로 옮겨지는 장대번호
# def hanoi_tower(n, frm, otr, to) :
#     if n == 1 :
#         print(frm, to)
#     else :
#         hanoi_tower(n-1, frm, to, otr)
#         print(frm, to)
#         hanoi_tower(n-1, otr, frm, to)

# n = int(sys.stdin.readline().rstrip())
# print((2**n)-1)
# hanoi_tower(n,1,2,3)

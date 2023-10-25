import sys

h,w,n,m = map(int, sys.stdin.readline().split())

cnt = 0
one_row = 0

# 한 행에 m칸씩 띄어서 앉은 총 사람 수를 구한다
for _ in range(0, w, m+1) :
    one_row += 1

# 그 후, 총 n행씩 띄어서 그 행에 앉은 사람 수를 누적 시킨다
for _ in range(0, h, n+1) :
    cnt += one_row
    
print(cnt)
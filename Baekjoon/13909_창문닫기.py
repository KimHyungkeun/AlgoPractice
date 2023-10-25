# 20230629 재풀이(Retry)
import sys

n = int(sys.stdin.readline().rstrip())

cnt = 0
t = 3
while n > 0 :
    n -= t
    t += 2
    cnt += 1

print(cnt)









# 정답은 맞았으나 질문게시판 힌트봤음
# import sys

# n = int(sys.stdin.readline().rstrip())

# 가설 1 : n이 늘어날수록 100 10000 100000000과 같이 0의 갯수가 2의 제곱수만큼 커진다 (실패)
# n = int(sys.stdin.readline().rstrip())
# cnt = 0
# t = 2

# while n >= 0 :
#     num_str = 1 + t
#     n -= num_str
#     t *= 2
#     cnt += 1

# print(cnt)

# 가설 2 : n이 늘어날수록 100 10000 1000000 과 같이 0의 갯수가 2의 배수만큼 커진다
# tmp = [0] * n

# 가설2 테스트
# for i in range(1, n+1) :    
#     for j in range(i-1, n, i) :
#         if (j+1) % i == 0 :
#             if tmp[j] == 0 :
#                 tmp[j] = 1
#             else :
#                 tmp[j] = 0 
# print(str(i) + " : ", tmp)

# cnt = 0
# t = 2

# while n > 0 :
#     num_str = 1 + t
#     n -= num_str
#     t += 2
#     cnt += 1

# print(cnt)





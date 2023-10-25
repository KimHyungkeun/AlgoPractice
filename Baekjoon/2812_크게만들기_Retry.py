# 정답참고 
# https://velog.io/@joniekwon/Python-%EB%B0%B1%EC%A4%80-2812%EB%B2%88-%ED%81%AC%EA%B2%8C-%EB%A7%8C%EB%93%A4%EA%B8%B0
import sys

n, k = map(int, sys.stdin.readline().split())
numbers = sys.stdin.readline().rstrip()
stack = []

for i in range(n) :
    while stack and stack[-1] < numbers[i] and k > 0 :
        stack.pop()
        k -= 1
    stack.append(numbers[i])

if k > 0 :
    print(''.join(stack[:-k]))
else :
    print(''.join(stack))

# 231010 72%에서 오답
# import sys

# n, k = map(int, sys.stdin.readline().split())
# numbers = sys.stdin.readline().rstrip()
# stack = []

# for i in range(n) :
#     if not stack :
#         stack.append(numbers[i])
#     else :
#         if int(stack[-1]) < int(numbers[i]) :
#             while stack and int(stack[-1]) < int(numbers[i]) :
#                 stack.pop()
#                 k -= 1
#                 if k == 0 :
#                     break
#             stack.append(numbers[i])
#         else :
#             stack.append(numbers[i])
    
#     if k == 0 :
#         break

# for j in range(i+1, n) :
#     stack.append(numbers[j])

# print(''.join(stack))


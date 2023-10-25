# 230907 Retry Success
import sys

n, m = map(int, sys.stdin.readline().split())
score_list = list(map(int, sys.stdin.readline().split()))
student_list = []

for _ in range(m) :
    inputs = list(sys.stdin.readline().split())
    student_num = int(inputs[0])
    total = 0

    for i in range(1, len(inputs)) :
        if inputs[i] == 'O' :
            total += score_list[i-1] 
    
    student_list.append((student_num, total))

# 수험번호 순서대로 정렬
student_list.sort(key = lambda x : x[0])

# 점수가 가장 높은 순서대로 정렬
student_list.sort(key = lambda x : x[1], reverse=True)

print(student_list[0][0], student_list[0][1])

# 230906 solved but retry
# import sys

# n, m = map(int, sys.stdin.readline().split())
# score = list(map(int, sys.stdin.readline().split()))

# student_list = []

# for _ in range(m) :
#     total = 0
#     inputs = list(sys.stdin.readline().split())    
#     for i in range(1, len(inputs)) :
#         if inputs[i] == 'O' or inputs[i] == 'o':
#             total += score[i-1]
#     student_list.append((int(inputs[0]), total))

# # 수험번호가 작은순서대로 먼저 정렬
# student_list.sort(key = lambda x : x[0])


# # 점수가 가장 높은 순서대로 정렬
# student_list.sort(key = lambda x : x[1], reverse=True)


# print(student_list[0][0], student_list[0][1])
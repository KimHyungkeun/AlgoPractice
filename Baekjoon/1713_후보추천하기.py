# 230704 retry
import sys

n = int(sys.stdin.readline().rstrip())
total_recommend = int(sys.stdin.readline().rstrip())
recommend_list = list(map(int, sys.stdin.readline().split()))

recommend_dict = {}
survive_dict = {}

for r in recommend_list :
    if r not in recommend_dict and len(recommend_dict)+1 <= n:
        if survive_dict :
            for key in survive_dict.keys() :
                survive_dict[key] += 1
        recommend_dict[r] = 1
        survive_dict[r] = 1

    elif r not in recommend_dict and len(recommend_dict)+1 > n :
        for key in survive_dict.keys() :
            survive_dict[key] += 1

        min_val = min(recommend_dict.values())
        min_recommend_list = []
        for key in recommend_dict.keys() :
            if recommend_dict[key] == min_val :
                min_recommend_list.append(key)
        
        if len(min_recommend_list) >= 2 :
            max_survive_val = 0
            max_student = 0
            for m in min_recommend_list :
                if survive_dict[m] > max_survive_val :
                    max_survive_val = survive_dict[m]
                    max_student = m
            
            del recommend_dict[max_student]
            del survive_dict[max_student]

        else :
            del recommend_dict[min_recommend_list[0]]
            del survive_dict[min_recommend_list[0]]
        
        recommend_dict[r] = 1
        survive_dict[r] = 1
    
    else :
        recommend_dict[r] += 1
        for key in survive_dict.keys() :
            survive_dict[key] += 1

result = sorted(recommend_dict.keys())
for r in result :
    print(r, end=' ')

# 출력 예시 이해 안되서, 질문게시판 찾아봤음
# import sys

# n = int(sys.stdin.readline().rstrip())
# student_num = int(sys.stdin.readline().rstrip())
# student_list = list(map(int, sys.stdin.readline().split()))

# recommend_dict = {}
# survive_dict = {}
# result = []

# for student in student_list :

#     if len(survive_dict) :
#         for key in survive_dict.keys() :
#             survive_dict[key] += 1

#     # 게시판에 추천학생이 존재하면 추천수 증가
#     if student in result :
#         recommend_dict[student] += 1

#     # 게시판에 빈칸이 있고, 새로 추가가 가능한 학생일 경우
#     if student not in result and len(result)+1 <= n :
#         result.append(student)
#         recommend_dict[student] = 1
#         survive_dict[student] = 1
    
#     # 새로 추가해야하나 게시판에 빈칸이 없을 경우
#     if student not in result and len(result)+1 > n :
#         min_val = min(recommend_dict.values())
#         min_recommend = []
#         for key in recommend_dict.keys() :
#             if recommend_dict[key] == min_val :
#                 min_recommend.append(key)
        
#         # 추천수가 가장 적은 학생을 게시판에서 내림
#         if len(min_recommend) == 1 :
#             i = result.index(min_recommend[0])
#             result[i] = student
#             del recommend_dict[min_recommend[0]]
#             del survive_dict[min_recommend[0]]
#             recommend_dict[student] = 1
#             survive_dict[student] = 1

#         # 추천수가 가장 적은 학생 여럿 중, 게시판에 오래 머물렀던 학생을 게시판에서 내림
#         if len(min_recommend) > 1 :
#            max_survive = 0
#            max_student = 0

#            for m in min_recommend : 
#                 if survive_dict[m] > max_survive :
#                     max_survive = survive_dict[m]
#                     max_student = m

#            i = result.index(max_student)
#            result[i] = student
#            del recommend_dict[max_student]
#            del survive_dict[max_student]
#            recommend_dict[student] = 1
#            survive_dict[student] = 1
    
# # 오름차순 정렬
# result.sort()
# for r in result : 
#     print(r, end=' ')


    
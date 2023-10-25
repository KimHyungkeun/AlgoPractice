import sys

n = int(sys.stdin.readline())

country = {}
all_student = []
final_result = []
for _ in range(n) :
    con_num, stu_num, score = map(int, sys.stdin.readline().split())
    if con_num not in country :
        country[con_num] = 1
    all_student.append((con_num, stu_num, score))

# 점수를 기준으로 내림차순 정렬
all_student.sort(key = lambda x : x[2], reverse=True)

# 점수별로 금,은,동 순서로 랭크를 매기되, 한 국가에서 받을수있는 수상의 갯수는 최대 2개까지
for a in all_student :
    if country[a[0]] <= 2 :
        final_result.append(a)
        country[a[0]] += 1
    
    if len(final_result) == 3 :
        break

for f in final_result :
    print(f[0], f[1])


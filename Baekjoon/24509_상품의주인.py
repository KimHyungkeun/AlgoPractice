import sys

n = int(sys.stdin.readline().rstrip())
subject = {"kor":[], "eng":[], "math":[], "sci":[]}
answer = []

for _ in range(n) :
    stu, kor, eng, math, sci = map(int, sys.stdin.readline().split())
    subject["kor"].append((kor,stu))
    subject["eng"].append((eng,stu))
    subject["math"].append((math,stu))
    subject["sci"].append((sci,stu))

for key in subject.keys() :
    subject[key].sort(key = lambda x : x[1])
    subject[key].sort(key = lambda x : x[0], reverse=True)


for key in subject.keys() :
    for score in subject[key] :
        if score[1] not in answer :
            answer.append(score[1])
            break 
for a in answer :
    print(a, end=' ')
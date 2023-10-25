import sys

n = int(sys.stdin.readline())
students = []

for _ in range(n) :
    student = list(sys.stdin.readline().rstrip())
    student.reverse()
    students.append(''.join(student))

student_num_length = len(students[0])

for i in range(1, student_num_length+1) :
    stu_set = set({})
    for s in students :
        stu_set.add(s[0:i])
    if len(stu_set) == n :
        break

print(i)

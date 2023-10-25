# 30명 학생들 중 숙제를 내지않은 2명을 가려내는 코드
import sys

submit = {}
for i in range(1, 31) :
    submit[i] = False

for _ in range(28) :
    n = int(sys.stdin.readline().rstrip())
    submit[n] = True

for key in submit.keys() :
    if not submit[key] :
        print(key)
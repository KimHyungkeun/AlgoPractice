# 배열에 N개의 숫자들이 존재
# 그 중 숫자가 v인 갯수를 찾음
import sys

N = int(sys.stdin.readline().rstrip())
lists = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline().rstrip()) 

result = 0
for l in lists :
    if l == v :
        result += 1

print(result)
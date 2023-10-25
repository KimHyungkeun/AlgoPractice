# a가격의 물건을 b개 구입하고
# 이를 N번 반복
# 이때, 그 결과가 X와 같은지 판단
import sys

X = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

total = 0
for _ in range(N) :
    a, b = map(int, sys.stdin.readline().split())
    total += (a*b)

if total == X :
    print("Yes")
else :
    print("No")
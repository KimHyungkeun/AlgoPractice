import sys
# 대칭 차집합
# set1의 차집합과 set2의 차집합을 합집합한 갯수를 구하기
a, b = map(int, sys.stdin.readline().split())
set1 = set(map(int, sys.stdin.readline().split()))
set2 = set(map(int, sys.stdin.readline().split()))

result1 = set1 - set2
result2 = set2 - set1
result = result1 | result2
print(len(result))
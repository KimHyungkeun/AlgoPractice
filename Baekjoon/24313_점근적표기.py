# O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline().rstrip())
n0 = int(sys.stdin.readline().rstrip())

def f(a1, a0, n) :
    return a1*n + a0

def g(n) :
    return n

flag = True
for n in range(n0, 100) :
    if f(a1, a0, n) <= c * g(n) :
        continue
    else :
        flag = False
        break

if flag :
    print(1)
else :
    print(0)
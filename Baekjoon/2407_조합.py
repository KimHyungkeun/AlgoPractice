import sys

n,m = map(int, sys.stdin.readline().split())

n_fact = 1
m_fact = 1
n_minus_m_fact = 1

for i in range(1, n+1) :
    n_fact *= i

for i in range(1, m+1) :
    m_fact *= i

for i in range(1, n-m+1) :
    n_minus_m_fact *= i

print(n_fact // (m_fact * n_minus_m_fact))
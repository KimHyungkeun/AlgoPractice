import sys

a,b,c,d,e,f = map(int, sys.stdin.readline().split())

x = (e*c - f*b) // (a*e - d*b)
y = (d*c - a*f) // (b*d - e*a)

print(x, y)
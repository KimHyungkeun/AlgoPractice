import sys

num1, num2 = map(int, sys.stdin.readline().split())
num3, num4 = map(int, sys.stdin.readline().split())

def gcd(a, b) :
    while b > 0 :
        a, b = b, a % b
    return a

def lcm(a, b) :
    return a * b // gcd(a, b)

bunmo = lcm(num2, num4)
to_multiple1 = bunmo // num2
to_multiple2 = bunmo // num4

bunza = (num1 * to_multiple1) + (num3 * to_multiple2)

giyak = gcd(bunza, bunmo)
bunza //= giyak
bunmo //= giyak

print(bunza, bunmo)


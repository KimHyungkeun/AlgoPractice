import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n) :
    c = int(sys.stdin.readline().rstrip())

    quarter = c // 25
    c %= 25

    dime = c // 10
    c %= 10

    nickel = c // 5
    c %= 5

    penny = c

    print(quarter, dime, nickel, penny)
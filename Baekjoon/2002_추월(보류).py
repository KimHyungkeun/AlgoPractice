import sys

n = int(sys.stdin.readline().rstrip())
before = []
after = []

for _ in range(n) :
    before.append(sys.stdin.readline().rstrip())
for _ in range(n) :
    after.append(sys.stdin.readline().rstrip())

cnt = 0
idx = 0

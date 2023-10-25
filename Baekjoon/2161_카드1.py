import sys
from collections import deque

n = int(sys.stdin.readline())

cards = []
flow = []

for i in range(n) :
    cards.append(i+1)
q = deque(cards)

while len(q) != 1 :
    flow.append(q.popleft())
    q.append(q.popleft())
    print(flow[-1], end=' ')
print(q[0])



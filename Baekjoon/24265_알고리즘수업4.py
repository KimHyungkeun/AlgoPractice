# 수행횟수 : O((n^2 - n) / 2)
# 시간복잡도 최고차수: 2

import sys

n = int(sys.stdin.readline().rstrip())

print((n * (n-1)) // 2)
print(2)
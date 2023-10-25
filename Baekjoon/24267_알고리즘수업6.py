# 수행횟수 : O(n^3 / 6)
# 시간복잡도 최고차수: 3

import sys

n = int(sys.stdin.readline().rstrip())

result = ((n-2) * (n-1) * n) // 6
print(result)
print(3)
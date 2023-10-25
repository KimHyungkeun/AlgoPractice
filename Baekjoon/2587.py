import sys

arr = []
for _ in range(5) :
    n = int(sys.stdin.readline().rstrip())
    arr.append(n)

arr.sort()
avg = sum(arr) // 5
mid = arr[2]

print(avg)
print(mid)

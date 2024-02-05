import sys

# 출처 : https://hae-sooo97.tistory.com/59

n, l = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
start = arr[0]
cnt = 1

for i in arr[1:] :
    if (i+0.5) - (start-0.5) <= l :
        continue
    else :
        start = i
        cnt += 1

print(cnt)
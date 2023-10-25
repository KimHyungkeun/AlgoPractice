import sys

serial_tuple = []
n = int(sys.stdin.readline().rstrip())

for _ in range(n) :
    serial = sys.stdin.readline().rstrip()
    cnt = 0
    for s in serial :
        if '0' <= s <= '9' :
            cnt += int(s)
    serial_tuple.append((serial, cnt))

# 사전순 비교
serial_tuple.sort()

# 자리수 합 순으로 비교
serial_tuple.sort(key = lambda x : x[1])

# 길이가 짧은것을 먼저 비교
serial_tuple.sort(key = lambda x : len(x[0]))

for result in serial_tuple :
    print(result[0])

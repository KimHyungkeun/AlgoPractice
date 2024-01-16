import sys

n = int(sys.stdin.readline().rstrip())
meeting_time = []

for _ in range(n) :
    start, end = map(int, sys.stdin.readline().split())
    meeting_time.append((start, end))

meeting_time.sort(key=lambda x : x[0])
meeting_time.sort(key=lambda x : x[1])


cnt = 0
end_time = -1
for i in range(len(meeting_time)) :
    if end_time <= meeting_time[i][0] :
        end_time = meeting_time[i][1]
        cnt += 1

print(cnt)

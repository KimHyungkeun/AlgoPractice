# 230925 Retry Success
import sys

n = int(sys.stdin.readline().rstrip())

time_list = []
for _ in range(n) :
    hour, minute, sec = map(int, sys.stdin.readline().split())
    times = int(hour)*3600 + int(minute)*60 + int(sec)
    time_list.append(times)

time_list.sort()

for t in time_list :
    result = t

    result_hour = result // 3600
    result -= (result_hour * 3600)

    result_min = result // 60
    result -= (result_min * 60)

    result_sec = result

    print(result_hour, result_min, result_sec)

# 230922 4%에서 틀림
# import sys

# n = int(sys.stdin.readline().rstrip())

# time_list = []
# result = []
# for _ in range(n) :
#     hour, minuite, sec = map(int, sys.stdin.readline().split())
#     time_list.append(hour * 3600 + minuite * 60 + sec)

# time_list.sort()

# for t in time_list :
#     to_hour = (t // 3600)
#     str_hour = str(to_hour)
#     t -= (to_hour * 3600)

#     to_min = (t // 60)
#     str_min = str(to_min)
#     t -= (to_min * 60)
 
#     to_sec = t
#     str_sec = str(to_sec)
    
#     print(str_hour, str_min, str_sec)
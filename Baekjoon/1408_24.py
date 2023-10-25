# 230922 Retry Success
import sys

start_time = sys.stdin.readline().rstrip()
end_time = sys.stdin.readline().rstrip()

start_to_sec = int(start_time.split(":")[0]) * 3600 + int(start_time.split(":")[1]) * 60 + int(start_time.split(":")[2])
end_to_sec = int(end_time.split(":")[0]) * 3600 + int(end_time.split(":")[1]) * 60 + int(end_time.split(":")[2])

if start_to_sec > end_to_sec :
    end_to_sec += 86400

remain_time = end_to_sec - start_to_sec

hour = remain_time // 3600
remain_time -= ( hour * 3600 )

minute = remain_time // 60
remain_time -= ( minute * 60 )

sec = remain_time

if hour < 10 :
    str_hour = '0' + str(hour)
else :
    str_hour = str(hour)

if minute < 10 :
    str_minute = '0' + str(minute)
else :
    str_minute = str(minute)

if sec < 10 :
    str_sec = '0' + str(sec)
else :
    str_sec = str(sec)

print(str_hour + ":" + str_minute + ":" + str_sec)

# 230918 Retry
# import sys
# start = sys.stdin.readline().rstrip()
# end = sys.stdin.readline().rstrip()

# start = start.split(":")
# end = end.split(":")

# start_to_sec = int(start[0]) * 3600 + int(start[1]) * 60 + int(start[2])
# end_to_sec = int(end[0]) * 3600 + int(end[1]) * 60 + int(end[2])

# if end_to_sec < start_to_sec :
#     end_to_sec += 86400
# remain_sec = end_to_sec - start_to_sec

# hour = remain_sec // 3600
# remain_sec -= (hour * 3600)

# minuite = remain_sec // 60
# remain_sec -= (minuite * 60)

# str_hour = str(hour)
# if len(str_hour) == 1 :
#     str_hour = '0' + str_hour

# str_miuite = str(minuite)
# if len(str_miuite) == 1 :
#     str_miuite = '0' + str_miuite

# str_sec = str(remain_sec)
# if len(str_sec) == 1 :
#     str_sec = '0' + str_sec

# print(str_hour + ":" + str_miuite + ":" + str_sec)
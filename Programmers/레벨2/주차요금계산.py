import math 

def solution(fees, records):
    result = []
    time_accum_dict = {}

    for r in records :
        if r.split()[1] not in time_accum_dict :
            time_accum_dict[r.split()[1]] = 0
    car_num_list = list(time_accum_dict.keys())
    
    
    for car_num in car_num_list :
        start_time, end_time = 0,0
        in_cnt = 0
        out_cnt = 0
        for r in records :
            r_split = r.split()
            if r_split[1] == car_num and r_split[2] == 'IN' :
                time = r_split[0].split(":")
                start_time = int(time[0]) * 60 + int(time[1])
                in_cnt += 1
            if r_split[1] == car_num and r_split[2] == 'OUT' :
                time = r_split[0].split(":")
                end_time = int(time[0]) * 60 + int(time[1])
                out_cnt += 1
            
            if in_cnt == out_cnt :
                time_accum_dict[car_num] += (end_time - start_time)
                start_time, end_time = 0,0

        if in_cnt != out_cnt :
            time_accum_dict[car_num] += (23 * 60 + 59 - start_time)

    result_car_time= sorted(list(time_accum_dict.items()), key = lambda x : int(x[0]))
    
    for r in result_car_time :
        if r[1] <= fees[0] :
            result.append(fees[1])
        else :
            val = fees[1] + ( math.ceil((r[1] - fees[0]) / fees[2]) ) * fees[3]
            result.append(val)


    print(result)
    return result

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
solution(fees, records)
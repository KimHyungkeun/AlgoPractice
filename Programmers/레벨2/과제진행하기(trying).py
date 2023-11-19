# 230706 54% 성공
def solution(plans):
    complete = []
    wait = []

    for p in plans :
        p[1] = int(p[1].split(":")[0]) * 60 + int(p[1].split(":")[1])
        p[2] = int(p[2])
    
    plans.sort(key = lambda x : x[1], reverse=True)
    
    item = plans.pop()
    cur_subject = item[0]
    cur_time = item[1]
    play_time = item[2]

    is_last = False
    while wait or plans :
        # plans에 값이 있을때만 확인
        if plans :
            next = plans.pop()
            if not plans :
                is_last = True
        
            if not wait :
                if cur_time + play_time <= next[1] :
                    complete.append(cur_subject)
                    cur_time += play_time

                else :
                    play_time -= (next[1] - cur_time)
                    wait.append([cur_subject, play_time])
                    cur_time = next[1]
            
            else :
                if cur_time + play_time < next[1] :
                    complete.append(cur_subject)
                    cur_time += play_time
                    wait[-1][1] -= play_time
                    if wait[-1][1] <= 0 :
                        complete.append(wait.pop()[0])
                
                elif cur_time + play_time == next[1] :
                    complete.append(cur_subject)
                    cur_time += play_time

                else :
                    play_time -= (next[1] - cur_time)
                    wait.append([cur_subject, play_time])
                    cur_time = next[1]
              
            
            cur_subject = next[0]
            cur_time = next[1]
            play_time = next[2]

            print(cur_time, next, complete, wait)

        if is_last :
            complete.append(cur_subject)
            while wait :
                complete.append(wait.pop()[0])

            
    print(complete)
    return complete

# plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]/
# plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
# plans = [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]
plans = [["korean", "11:00", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
solution(plans)
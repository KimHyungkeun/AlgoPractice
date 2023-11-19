# 20230327 성공코드
def solution(book_time):
    answer = 0
    room = []
    
    book_time.sort(key = lambda x : x[0])
    
    for b in book_time :
        change_flag = False
        if not room :
            room.append(b)
        else :
            for i in range(len(room)) :
                end_minute = int(room[i][1].split(":")[0])*60 + int(room[i][1].split(":")[1])
                if end_minute + 10 <= int(b[0].split(":")[0])*60 + int(b[0].split(":")[1]) :
                    room[i] = b
                    change_flag = True
                    break
            if not change_flag :
                room.append(b)
    answer = len(room)
    return answer

# 20230218 성공코드
def solution(book_time):
    answer = 0
    rooms = []
    
    for b in book_time :
        b[0] = (int(b[0].split(":")[0]) * 60 + int(b[0].split(":")[1]))
        b[1] = (int(b[1].split(":")[0]) * 60 + int(b[1].split(":")[1]))
    book_time.sort(key = lambda x : x[0])

    for b in book_time :
        flag = False
        if not rooms :
            rooms.append(b)
        else :
            for r in range(len(rooms)) :
                if rooms[r][1] + 10 <= b[0] :
                    rooms[r] = b
                    flag = True
                    break
            if not flag :
                rooms.append(b)
            # print(rooms)
            
    answer = len(rooms)
    return answer

# 20230218 실패코드
def solution(book_time):
    answer = 0
    rooms = []
    
    for b in book_time :
        b[0] = (int(b[0].split(":")[0]) * 60 + int(b[0].split(":")[1]))
        b[1] = (int(b[1].split(":")[0]) * 60 + int(b[1].split(":")[1]))
    book_time.sort(key = lambda x : x[0])
    
    for b in book_time :
        flag = False
        if not rooms :
            rooms.append(b)
        else :
            for r in rooms :
                if r[1] + 10 <= b[0] :
                    r = b
                    flag = True
                    break
            if not flag :
                rooms.append(b)
            
    answer = len(rooms)
    return answer
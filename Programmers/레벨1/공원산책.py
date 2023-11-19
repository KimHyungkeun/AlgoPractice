def solution(park, routes):
    answer = []
    start_pos = []
    row_length = len(park[0])
    
    for i in range(len(park)) :
        for j in range(row_length) :
            if park[i][j] == 'S' :
                start_pos = [i,j]
                break
        if start_pos :
            break
    
    # 만약 공원을 벗어나거나 장애물을 맞닥뜨리는 경우의 명령은 무시한다
    for r in routes :
        direct = r.split(" ")[0]
        distance = int(r.split(" ")[1])
        not_execute = False
        
        # 동쪽으로 distance만큼 이동
        if direct == 'E' :
            for d in range(distance) :
                if start_pos[1] + 1 == row_length or park[start_pos[0]][start_pos[1]+1] == 'X' :
                    not_execute = True
                    break
                start_pos[1] += 1

            if not_execute :
                start_pos[1] -= d

        # 서쪽으로 distance만큼 이동
        elif direct == 'W' :
            for d in range(distance) :
                if start_pos[1] - 1 < 0 or park[start_pos[0]][start_pos[1]-1] == 'X' :
                    not_execute = True
                    break
                start_pos[1] -= 1
            if not_execute :
                start_pos[1] += d

        # 남쪽으로 distance만큼 이동
        elif direct == 'S' :
            for d in range(distance) :
                if start_pos[0] + 1 == len(park) or park[start_pos[0]+1][start_pos[1]] == 'X' :
                    not_execute = True
                    break
                start_pos[0] += 1
            if not_execute :
                start_pos[0] -= d

        # 북쪽으로 distance만큼 이동
        else :
            for d in range(distance) :
                if start_pos[0] - 1 < 0 or park[start_pos[0]-1][start_pos[1]] == 'X' :
                    not_execute = True
                    break
                start_pos[0] -= 1
            if not_execute :
                start_pos[0] += d
        
    
    answer = start_pos
    return answer

park = ["SOO","OXX","OOO"]
routes = ["E 2","S 2","W 1"]	
solution(park, routes)
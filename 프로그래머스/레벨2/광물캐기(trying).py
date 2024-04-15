# 순서
# 1. case_list에 광물을 5개씩 묶음으로 한 부분 리스트를 넣는다.
# 2. 부분 리스트 내에서 가장 등급이 높은 광물을 찾아낸다.
# 3. 해당 광물로 만든 곡괭이를 picks에서 고른다 (0:다이아, 1:아이언, 2: 스톤)
# 4. 만약 해당 광물 곡괭이가 0개이면 그다음 등급의 곡괭이를 고른다
# 5. 전부 채굴했거나 또는 사용할 곡괭이가 없으면 그 시점에서 종료

from collections import deque
def solution(picks, minerals):
    sec = 0
    case_list = []
    for i in range(0, len(minerals), 5) :
        case_list.append(minerals[i:i+5])
    for c in case_list :
        if sum(picks) == 0 :
            break

        q = deque(c)
        tools = -1
        
        if "diamond" in q :
            if picks[0] > 0 :
                picks[0] -= 1
                tools = 0
            elif picks[1] > 0 :
                picks[1] -= 1
                tools = 1
            else :
                picks[2] -= 1
                tools = 2

        elif "iron" in q :
            if picks[1] > 0 :
                picks[1] -= 1
                tools = 1
            else :
                picks[2] -= 1
                tools = 2 
            
        else :
            if picks[2] > 0 :
                picks[2] -= 1
                tools = 2

    
        if tools == 0 :
            while q :
                q.popleft()
                sec += 1
        if tools == 1 :
            while q : 
                gem = q.popleft()
                if gem == "diamond" :
                    sec += 5
                else :
                    sec += 1
        if tools == 2 :
            while q :
                gem = q.popleft()
                if gem == "diamond" :
                    sec += 25
                elif gem == "iron" :
                    sec += 5
                else :
                    sec += 1

    return sec


picks = [0,1,1]
minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
solution(picks, minerals)
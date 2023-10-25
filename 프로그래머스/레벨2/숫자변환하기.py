from collections import deque
def solution(x, y, n):
    
    # 같은 숫자면 변환할 필요가 없으므로 0
    if x == y :
        return 0
    
    answer = 1
    flag = False
    
    result = []
    if y - n >= x :
        result.append(y - n)
    if y % 2 == 0 :
        result.append(y // 2)
    if y % 3 == 0 :
        result.append(y // 3)
    
    q = deque(result) 
    tmp = []
    
    # BFS형태로 아래와 같이 2x, 3x, x+n에 대한 값이 y와 같은지 확인
    while q :
        
        if x in q :
            flag = True
            break
        
        val = q.popleft()
        if val - n >= x :
            tmp.append(val - n)
        if val % 2 == 0 :
            tmp.append(val // 2)
        if val % 3 == 0 :
            tmp.append(val // 3)
        
        if not q and tmp:
            answer += 1
            tmp = list(set(tmp))
            q = deque(tmp)
            tmp = []
            
        
    if flag :
        return answer
    else :
        return -1